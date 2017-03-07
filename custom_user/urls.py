from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^userslist/$', views.userslist, name='userslist'),
]