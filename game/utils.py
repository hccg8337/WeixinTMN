import datetime

from models import Game, GameState, GameType
from node.models import Node, NodeState


def get_games():
    return Game.objects.all().filter(type=GameType.INSTANCE)


def get_game_state(game):
    now = datetime.datetime.now()
    nodename = ''
    if game.state != GameState.DEFAULT:
        return game.state, nodename

    r = Node.objects.all().filter(gameid=game).exclude(state=NodeState.NOUSE)
    if not r:
        return GameState.EMPTY, nodename

    s = GameState.NOTSTART
    done_num = 0
    for i in r:
        if i.state == NodeState.BROKEN:
            return GameState.BROKEN, i.name
        if s != GameState.OVERTIME and i.state != NodeState.DONE and i.deadline and i.deadline < now:
            s = GameState.OVERTIME
            nodename = i.name
            continue
        if s != GameState.OVERTIME and i.state == NodeState.DONE:
            s = GameState.PROCESSING
            done_num += 1
    if s == GameState.OVERTIME:
        return s, nodename
    if done_num == len(r):
        return GameState.DONE, ''

    return s, nodename


def get_games_with_user(user):
    r = user.games.all()
    return r


def get_user_related_to_game(game):
    r = game.user2game.all()
    return r