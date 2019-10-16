from django.shortcuts import render
from app import forms

# Create your views here.


def get_recruit_form(request):
    context = {
        'from': forms.Recruit
    }

    return render(request, 'app/recruit_form.html', context)


def save_recruit_form(request):
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print(request.body.decode('utf-8'))
    return render(request, 'app/main_page.html')
