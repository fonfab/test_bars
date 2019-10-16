from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from app import views


urlpatterns = [
    url(r'recruit_form', views.get_recruit_form),
    url(r'save_recruit_form', views.save_recruit_form),

]