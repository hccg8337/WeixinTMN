from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^setmodules/$', views.set_modules, name='set_modules'),
]