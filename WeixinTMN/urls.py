# -*- coding:utf-8 -*-

"""WeixinTMN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


from . import views


urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^syncdb/$', views.syncdb),
    #step 3
    url(r'^init/$', views.init),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^action/', include('action.urls')),
    url(r'^config/', include('config.urls')),
    url(r'^customuser/', include('custom_user.urls')),
    url(r'^game/', include('game.urls')),
    url(r'^gamestemplate/', include('games_template.urls')),
    url(r'^log/', include('log.urls')),
    url(r'^module/', include('module.urls')),
    url(r'^msg/', include('msg.urls')),
    url(r'^node/', include('node.urls')),
    url(r'nodestemplate/', include('nodes_template.urls')),
    url(r'^role/', include('role.urls')),
    url(r'usersgroup/', include('users_group.urls')),
    url(r'weixininterface/', include('weixin_interface.urls')),
]
