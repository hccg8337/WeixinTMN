from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^refreshaccesstoken/$', views.refresh_access_token, name='refresh_access_token'),
    #step 2 menu
    url(r'^setmenu/$', views.set_menu, name='set_menu'),
    # index
    url(r'^authtoindex/$', views.auth_to_index, name='auth_to_index'),
    #step 1
    url(r'^checksignature/$', views.check_signature, name='check_signature'),
]