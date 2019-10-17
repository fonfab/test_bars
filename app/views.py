from django.shortcuts import render, redirect
from app import forms
from app import models

# Create your views here.


def get_recruit_form(request):
    if request.method == 'POST':
        form = forms.Recruit(request.POST)
        if form.is_valid():
            form.save()

        return redirect('recruit_test')
    else:
        return render(request, 'app/recruit_form.html', {'form': forms.Recruit})


def get_recruit_test(request):
    print()
    return render(request, 'app/main_page.html')
