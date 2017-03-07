from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^readnodestemplateconfig/$', views.read_nodestemplate_config, name='read_nodestemplate_config'),
]