from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^setroles/$', views.set_roles, name='set_roles'),
]