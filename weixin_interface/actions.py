import datetime

from WeixinTMN.utils import has_permission
from game.models import Game, GameState
from action.models import ActionNoId
from node.models import NodeState
from msg.models import MsgStateType
import game.utils


def get_statistics(user, date):
    all = 0
    done = 0
    broken = 0
    emergency = 0
    start = datetime.datetime.combine(date, datetime.time.min)
    end = datetime.datetime.combine(date, datetime.time.max)
    if has_permission(user, ActionNoId.NO005002, ActionNoId.NO005003):
        if has_permission(user, ActionNoId.NO005002):
            r = Game.objects.all().filter(workstarttime__range=(start, end), state__in=[GameState.DEFAULT, GameState.DONE])
        elif has_permission(user, ActionNoId.NO005003):
            r = user.games.all().filter(workstarttime__range=(start, end), state__in=[GameState.DEFAULT, GameState.DONE])
        all = 0
        done = 0
        broken = 0
        emergency = 0
        for i in r:
            s, name = game.utils.get_game_state(i)
            if s in [GameState.CANCELLED, GameState.NOTSTART]:
                continue
            all += 1
            if s in [GameState.DONE]:
                done += 1
            if s in [GameState.BROKEN]:
                broken += 1
            if s in [GameState.BROKEN, GameState.EMPTY, GameState.OVERTIME]:
                emergency += 1
    else:
        if has_permission(user, ActionNoId.NO004017):
            r = Game.objects.all().filter(workstarttime__range=(start, end),
                                          state__in=[GameState.DEFAULT, GameState.DONE])
            r = user.nodes.all().filter(gameid__in=r)
            all = 0
            done = 0
            broken = 0
            emergency = 0
            for i in r:
                if i.state in [NodeState.NOUSE]:
                    continue
                all += 1
                if i.state in [NodeState.DONE]:
                    done += 1
                if i.state in [NodeState.BROKEN]:
                    broken += 1
                    emergency += 1
    msg_all = user.msgstate2user.all().count()
    msg_notread = user.msgstate2user.all().filter(state=MsgStateType.NOTREAD).count()
    total = round(done / all, 2) if all > 0 else 0
    return total, broken, emergency, msg_notread, msg_all