from django.conf.urls import url
from django.contrib import admin
from app import views


urlpatterns = [
    url(r'recruit_form', views.get_recruit_form, name='recruit_form'),
    url(r'recruit_test', views.get_recruit_test, name='recruit_test'),
    url(r'sith_list', views.get_sith_list, name='sith_list'),
    url(r'list_recruit', views.get_recruit_list, name='list_recruit'),
    url(r'recruit', views.set_recruit, name='recruit'),
]