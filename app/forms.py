from django.forms import ModelForm
# from django.contrib.auth import (get_user_model, authenticate, password_validation)
from django import forms
from app import models


class Recruit(forms.ModelForm):
    class Meta:
        model = models.Recruit
        fields = ('name', 'planet', 'age', 'email')

        name_errors = {
            'required': "Введите ваше имя"
        }

        planet_errors = {
            'required': "Введите название вашей планеты"
        }

        age_errors = {
            'required': "Введите ваш возраст"
        }

        email_errors = {
            'required': "Введите ваш возраст"
        }

        name = forms.CharField(label='Имя рекрутера', error_messages=name_errors)
        planet = forms.CharField(label='Планета обитания', error_messages=planet_errors)
        age = forms.IntegerField(label='Возраст', error_messages=age_errors)
        email = forms.EmailField(label='Адресс электронной почты', error_messages=email_errors)

        def __init__(self, *args, **kwargs):
            self.user = None
            super().__init__(*args, **kwargs)

        def clean(self):
            self.name = self.cleaned_data.get('name', '')
            self.planet = self.cleaned_data.get('planet', '')
            self.age = self.cleaned_data.get('age', '')
            self.email = self.cleaned_data.get('email', '')
