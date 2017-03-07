# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^setactions/$', views.set_actions, name='set_actions'),
]