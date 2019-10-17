from django.shortcuts import render, redirect
from app import forms
from app import models

# Create your views here.


def get_recruit_form(request):
    recruit = ''
    if request.method == 'POST':
        form = forms.Recruit(request.POST)
        if form.is_valid():
            form.clean()
            recruit = form.save()

        request.session.update({'rec_id': recruit.id})
        print(request.session.__dict__)

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
        print(request.GET)

        context = {
            'list': models.TestTrials.objects.get(id_order=1).questions.all()
        }
        print()
        return render(request, 'app/test.html', context)
