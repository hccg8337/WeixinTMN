# -*- coding:utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^readgamestemplateconfig/$', views.read_gamestemplate_config, name='read_gamestemplate_config'),#更新比赛模板信息
]