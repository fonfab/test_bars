from django.shortcuts import render, redirect
# from django.core.mail import send_mail
from app import forms
from app import models
from app.app_methods import do_request_sql


def get_recruit_form(request):
    if request.method == 'POST':
        name = request.POST.get("name", "")
        planet = request.POST.get("planet", "")
        age = request.POST.get("age", "")
        email = request.POST.get("email", "")

        sql_str = """
            insert into app_Recruit (name, planet, age, email, shadow_hands_id)
            values ('{0}', '{1}', '{2}', '{3}', NULL)
        """.format(name, planet, age, email)
        do_request_sql(sql_str)
        recruit_id = do_request_sql("SELECT max(id) FROM app_Recruit")

        # recruit = ''
        # form = forms.Recruit(request.POST)
        #
        # if form.is_valid():
        #     form.clean()
        #     recruit = form.save()
        #
        # print(recruit.id)
        # request.session.update({'rec_id': recruit.id})
        #
        # return redirect("recruit_test")

        sql_str = """
            select id, name from app_question where id in 
            (select question_id from app_testtrials_questions where testtrials_id = 1)
        """
        res = do_request_sql(sql_str)

        res_list = [{"id": item[0], "name": item[1]}
                    for item in res]

        context = {
            'recruit_id': recruit_id[0][0],
            'list': res_list
            # 'list': models.TestTrials.objects.get(id_order=1).questions.all()
        }

        return render(request, 'app/test.html', context)
    else:
        return render(request, 'app/recruit_form.html', {'form': forms.Recruit})


def get_recruit_test(request):
    if request.method == 'POST':
        rec_id = request.POST.get('recruit_id', '')
        # recruit = models.Recruit.objects.get(id=rec_id)

        # questions = models.TestTrials.objects.get(id_order=1).questions.all()
        # for item in questions:
        #     answer = request.POST.get(item.id.__str__(), '')
        #     models.QuestionAsk(recruit=recruit, question=item, answer=answer).save()

        sql_str = "select question_id from app_testtrials_questions where testtrials_id = 1"
        res = do_request_sql(sql_str)
        print(res)

        for item in res:
            answer = request.POST.get(str(item[0]), '')
            sql_str = """
                insert into app_questionask (question_id, recruit_id, answer)
                values ('{0}', '{1}', '{2}')
                """.format(item[0], rec_id, answer)
            do_request_sql(sql_str)

        return redirect('main')


def get_sith_list(request):
    res = do_request_sql("SELECT id, name FROM app_sith")
    res_list = [{'id': item[0], "name": item[1]} for item in res]
    # print(res_list)
    context = {
        'list': res_list
        # 'list': models.Sith.objects.all()
    }
    return render(request, "app/list_sith.html", context)


def get_recruit_list(request):
    sql_str_req = """
        select app_recruit.id, app_recruit.name from app_recruit
        where app_recruit.shadow_hands_id is NULL
    """
    sql_str_questions = """
        select app_question.name, app_questionask.answer 
        from app_question, app_questionask
        where app_questionask.recruit_id = '{}' 
            and  app_questionask.question_id = app_question.id

    """
    res = do_request_sql(sql_str_req)
    print(res)

    for item in res:
        ress = do_request_sql(sql_str_questions.format(item[0]))
        print(ress)


    recruit_answer = [
        {
            'recruit': {'id': item[0], 'name': item[1]},
            'answer': [
                {
                    'question': {'name': ans[0]},
                    'answer': ans[1]
                }
                for ans in do_request_sql(sql_str_questions.format(item[0]))
            ]
        }
        for item in res
    ]

    # print(recruit_answer)

    # recruit_answer = [{'recruit': item,
    #                    'answer': models.QuestionAsk.objects.filter(recruit=item)}
    #                   for item in models.Recruit.objects.filter(shadow_hands__isnull=True).all()]

    context = {
        'sith_id': request.GET.get('sith_id', ''),
        'list': recruit_answer
    }
    return render(request, "app/list_recruit.html", context)


def set_recruit(request):
    recruit_id = request.GET.get('recruit_id', '')
    sith_id = request.GET.get('sith_id', '')
    sith = models.Sith.objects.get(id=sith_id)

    sql_str = """
        select count(*) from app_recruit
        where shadow_hands_id = '{0}' 
            and id = '{1}'
    """.format(sith_id, recruit_id)
    res = do_request_sql(sql_str)

    # if models.Recruit.objects.filter(id=recruit_id, shadow_hands=sith).exists():
    if res[0][0] != 0:
        context = {
            'title': 'Ошибка',
            'msg': 'Данный пользователь уже завербован',
            'sith_id': sith_id,
        }
        return render(request, 'app/message.html', context)

    sql_str = """
        select count(*) from app_recruit
        where app_recruit.shadow_hands_id = '{0}'
    """.format(sith_id)
    res = do_request_sql(sql_str)

    # if len(models.Recruit.objects.filter(shadow_hands=sith)) > 3:
    if res[0][0] >= 3:
        context = {
            'title': 'Ошибка',
            'msg': 'У вас уже набрали достаточное количество рекрутов',
            'sith_id': sith_id,
        }
        return render(request, 'app/message.html', context)

    sql_str = """
        update app_recruit
        set shadow_hands_id = '{0}'
        where id = {1}
    """.format(sith_id, recruit_id)
    do_request_sql(sql_str)

    # recruit = models.Recruit.objects.get(id=recruit_id)
    # recruit.shadow_hands = sith
    # recruit.save()

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

    # send_mail(topic, msg, mail_from, mail_to)


def bonus(request):
    sql_str = """
        select app_sith.name, count(*) from app_recruit
        inner join app_sith on app_sith.id = app_recruit.shadow_hands_id
        group by app_sith.name
    """
    res = do_request_sql(sql_str)
    sql_str = """
        select app_sith.name, 0 from app_sith
        where app_sith.id not in (select shadow_hands_id from app_recruit where shadow_hands_id is not null)
    """
    res = res + do_request_sql(sql_str)
    sith_list = [
        {
            'sith': {'name': item[0]},
            'count': item[1]
        }
        for item in res
    ]

    # sith_list = [{'sith': item,
    #               'count': len(models.Recruit.objects.filter(shadow_hands=item))}
    #              for item in models.Sith.objects.all()]

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
