from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^flowindex/$', views.flow_index, name='flow_index'),
    url(r'^nodesflow/$', views.nodesflow, name='nodesflow'),
    url(r'^addnode/$', views.add_node, name='add_node'),
    url(r'^delnode/$', views.del_node, name='del_node'),
    url(r'^nodepermits/$', views.node_permits, name='node_permits'),
    url(r'^nodedetail/$', views.node_detail, name='node_detail'),
    url(r'^nodestate/$', views.node_state, name='node_state'),
    url(r'^nodeslist/$', views.nodeslist, name='nodeslist'),
    url(r'^checknodedeadline/$', views.check_node_deadline, name='check_node_deadline'),
    url(r'^updateflow/$', views.update_flow, name='update_flow'),
]