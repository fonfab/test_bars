from django.shortcuts import render, redirect
from django.core.mail import send_mail
from app import forms
from app import models


def get_recruit_form(request):
    recruit = ''
    if request.method == 'POST':
        form = forms.Recruit(request.POST)
        if form.is_valid():
            form.clean()
            recruit = form.save()

        request.session.update({'rec_id': recruit.id})
        # print(request.session.__dict__)

        return redirect("recruit_test")
    else:
        return render(request, 'app/recruit_form.html', {'form': forms.Recruit})


def get_recruit_test(request):
    if request.method == 'POST':
        questions = models.TestTrials.objects.get(id_order=1).questions.all()
        for item in questions:
            rec_id = request.session.get('rec_id', '')
            recruit = models.Recruit.objects.get(id=rec_id)
            answer = request.POST.get(item.id.__str__(), '')
            models.QuestionAsk(recruit=recruit, question=item, answer=answer).save()

        return redirect('main')
    else:
        # print(request.GET)

        context = {
            'list': models.TestTrials.objects.get(id_order=1).questions.all()
        }
        # print()
        return render(request, 'app/test.html', context)


def get_sith_list(request):
    context = {
        'list': models.Sith.objects.all()
    }
    return render(request, "app/list_sith.html", context)


def get_recruit_list(request):
    recruit_answer = [{'recruit': item, 'answer': models.QuestionAsk.objects.filter(recruit=item)}
                      for item in models.Recruit.objects.filter(shadow_hands__isnull=True).all()]

    context = {
        'sith_id': request.GET.get('sith_id', ''),
        'list': recruit_answer
    }
    return render(request, "app/list_recruit.html", context)


def set_recruit(request):
    recruit_id = request.GET.get('recruit_id', '')
    sith_id = request.GET.get('sith_id', '')
    sith = models.Sith.objects.get(id=sith_id)

    if models.Recruit.objects.filter(id=recruit_id, shadow_hands=sith).exists():
        context = {
            'title': 'Ошибка',
            'msg': 'Данный пользователь уже завербован',
            'sith_id': sith_id,
        }
        return render(request, 'app/message.html', context)

    if len(models.Recruit.objects.filter(shadow_hands=sith)) > 3:
        context = {
            'title': 'Ошибка',
            'msg': 'У вас уже набрали достаточное количество рекрутов',
            'sith_id': sith_id,
        }
        return render(request, 'app/message.html', context)

    recruit = models.Recruit.objects.get(id=recruit_id)
    recruit.shadow_hands = sith
    recruit.save()

    send_info_email()

    context = {
        'title': 'Удачно',
        'msg': 'Данному рекруту направлено сообщение о вербовке',
        'sith_id': sith_id,
    }
    return render(request, 'app/message.html', context)


def send_info_email():
    mail_from = 'info.services.kartli@gmail.com'
    mail_to = ['fonfabular@gmail.com']
    topic = 'Поздравляю вас завербовали'
    msg = 'Поздравляю вас завербовали'

    send_mail(topic, msg, mail_from, mail_to)


def bonus(request):
    sith_list = [{'sith': item, 'count': len(models.Recruit.objects.filter(shadow_hands=item))}
                 for item in models.Sith.objects.filter().all()]

    if request.GET.get('mod', '') == '1':
        sith_list = [item for item in sith_list if item['count'] != 0]
        context = {
            'mode': 0,
            'message': 'Перейти к списку со всеми ситхами',
            'list': sith_list
        }
    else:
        context = {
            'mode': 1,
            'message': 'Перейти к списку где нет ситхов без своих рук тени',
            'list': sith_list
        }
    return render(request, "app/bonus.html", context)
