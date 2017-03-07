from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^gameslist/$', views.gameslist, name='gameslist'),
    url(r'^selectgamestemplate/$', views.select_gamestemplate, name='select_gamestemplate'),
    url(r'^addgame/$', views.add_game, name='add_game'),
    url(r'^gamedetail/$', views.game_detail, name='game_detail'),
    url(r'^selectnodestemplate/$', views.select_nodestemplate, name='select_nodestemplate'),
    url(r'^cancelgame/$', views.cancel_game, name='cancel_game'),
]