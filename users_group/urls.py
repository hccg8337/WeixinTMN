from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^usersgroupslist/$', views.usersgroupslist, name='usersgroupslist'),
]