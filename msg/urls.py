from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^msgslistforcurrentuser/$', views.msgslist_for_currentuser, name='msgslist_for_currentuser'),
    url(r'^setmsgstructures/$', views.set_msg_structures, name='set_msg_structures'),
]