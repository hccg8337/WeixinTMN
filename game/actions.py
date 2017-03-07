import datetime

from django.core.exceptions import ObjectDoesNotExist

from WeixinTMN.utils import require_permission, has_permission, get_session_user, get_attrs
from models import GamePlace
from action.models import ActionNoId
from games_template.models import Date2GamesTemplate
from role.models import RoleType, Role
from game.models import GameType, Game, GameState
from node.models import NodeType, NodesLine, Node
import msg.utils
import utils
from httpclient import HttpClient
from WeixinTMN.models import LocalTimezone


@require_permission(*get_attrs(ActionNoId, 'NO005002', 'NO005003', 'NO004017'))
def get_games_by_date(request, date):
    #print('123')
    user = get_session_user(request)
    start = datetime.datetime.combine(date, datetime.time.min)
    end = datetime.datetime.combine(date, datetime.time.max)
    if has_permission(user, ActionNoId.NO005002):
        r = utils.get_games()
        r = r.filter(workstarttime__range=(start, end))
    elif has_permission(user, ActionNoId.NO005003):
        r = user.games.all()
        r = r.filter(workstarttime__range=(start, end))
        if not r and has_permission(user, ActionNoId.NO004017):
            r = []
            ret = utils.get_games()
            ret = ret.filter(workstarttime__range=(start, end))
            for i in ret:
                ns = i.game2node.all()
                for j in ns:
                    if j.user2node.all().filter(id=user.id):
                        r.append(i)
                        break
    else:
        #print('partner')
        ret = utils.get_games()
        ret = ret.filter(workstarttime__range=(start, end))
        ns = user.nodes.all()
        r = []
        for i in ret:
            ns = i.game2node.all()
            for j in ns:
                if j.user2node.all().filter(id=user.id):
                    r.append(i)
                    break
        #print(len(r))
    return r


@require_permission(*get_attrs(ActionNoId, 'NO005016'))
def select_gamestemplate_for_date(request, date, gamestemplate):
    Date2GamesTemplate.objects.update_or_create(date=date, defaults={'gamestemplate': gamestemplate})
    gameids = gamestemplate.gameids.all()
    for i in gameids:
        i.id = None
        i.type = GameType.INSTANCE
        i.workstarttime = datetime.datetime.combine(date, i.workstarttime.time())
        i.workendtime = datetime.datetime.combine(date, i.workendtime.time())
        i.gamestarttime = datetime.datetime.combine(date, i.gamestarttime.time())
        i.save()
    return 'success'


@require_permission(*get_attrs(ActionNoId, 'NO005001'))
@msg.utils.relate_game_to_user_msg
def add_game(request, game):
    workstarttime = game['workstarttime']
    workstarttime = datetime.datetime.strptime(workstarttime, '%Y%m%d%H%M%S')
    workendtime = game['workendtime']
    workendtime = datetime.datetime.strptime(workendtime, '%Y%m%d%H%M%S')
    r = Game.objects.all().filter(name=game['name'], workstarttime=workstarttime, workendtime=workendtime)
    if r:
        return 'game exist'
    game['workstarttime'] = workstarttime
    game['workendtime'] = workendtime
    game['gamestarttime'] = datetime.datetime.strptime(game['gamestarttime'], '%Y%m%d%H%M%S')
    game['type'] = GameType.INSTANCE
    g = Game(**game)
    g.save()
    u = Role.objects.get(id=RoleType.MANAGER).user2role.all()
    for i in u:
        i.games.add(g)
    return 'success'


@require_permission(*get_attrs(ActionNoId, 'NO005006', 'NO005007'))
def update_game_detail(request, game):
    user = get_session_user(request)
    id = int(game.pop('id'))
    if has_permission(user, ActionNoId.NO005006):
        pass
    else:
        games = user.games.all().filter(id=id)
        if not games:
            return 'no permission'
        else:
            games = games[0]
    if 'workstarttime' in game.keys() and game['workstarttime']:
        game['workstarttime'] = datetime.datetime.strptime(game['workstarttime'], '%Y%m%d%H%M%S')
        workstarttime = game['workstarttime']
    else:
        workstarttime = games.workstarttime
    if 'workendtime' in game.keys() and game['workendtime']:
        game['workendtime'] = datetime.datetime.strptime(game['workendtime'], '%Y%m%d%H%M%S')
        workendtime = game['workendtime']
    else:
        workendtime = games.workendtime
    if 'name' in game.keys():
        if Game.objects.all().filter(name=game['name'], type=GameType.INSTANCE, workstarttime=workstarttime, workendtime=workendtime).exclude(id=id):
            return 'name exist'
    if 'gamestarttime' in game.keys() and game['gamestarttime']:
        game['gamestarttime'] = datetime.datetime.strptime(game['gamestarttime'], '%Y%m%d%H%M%S')
    Game.objects.filter(id=id).update(**game)
    return 'success'


@require_permission(*get_attrs(ActionNoId, 'NO005004', 'NO005005'))
def get_game_detail(request, gameid):
    try:
        r = Game.objects.get(id=gameid)
    except ObjectDoesNotExist:
        r = 'game not exist'
    else:
        user = get_session_user(request)
        if has_permission(user, ActionNoId.NO005004):
            pass
        else:
            t = utils.get_games_with_user(user)
            t = t.filter(id=r.id)
            if not t:
                r = 'no permission'
    return r


@require_permission(*get_attrs(ActionNoId, 'NO005008', 'NO005009'))
def select_nodestemplate_for_game(request, game, nodestemplate):
    user = get_session_user(request)
    if has_permission(user, ActionNoId.NO005008):
        pass
    else:
        games = user.games.all().filter(id=id)
        if not games:
            return 'no permission'
    game.nodestemplateid = nodestemplate
    game.tops = nodestemplate.tops
    game.save()
    nodeids = nodestemplate.nodeids.all()
    m = {}
    for i in nodeids:
        t = i.id
        i.id = None
        i.type = NodeType.INSTANCE
        i.gameid = game
        i.save()
        m[str(t)] = i
    r = NodesLine.objects.all().filter(prevnodeid__in=nodeids)
    for i in r:
        i.id = None
        t = m[str(i.prevnodeid.id)]
        i.prevnodeid = t
        t = m[str(i.nextnodeid.id)]
        i.nextnodeid = t
        i.save()
    return 'success'


def get_places_from_web():
    hc = HttpClient('http://m.weather.com.cn/data5/city.xml', method='get')
    r = hc.rep
    r = r.split(',')
    for i in r:
        i = i.split('|')
        code = i[0]
        name = i[1]
        gp = GamePlace(name=name)
        gp.save()
        hc1 = HttpClient('http://m.weather.com.cn/data5/city%s.xml' % code, method='get')
        r1 = hc1.rep
        r1 = r1.split(',')
        for j in r1:
            j = j.split('|')
            GamePlace(name=j[1], parent=gp).save()


@require_permission(*get_attrs(ActionNoId, 'NO005012', 'NO005013'))
def cancel_game(request, game):
    user = get_session_user(request)
    if has_permission(user, ActionNoId.NO005012):
        pass
    else:
        games = user.games.all().filter(id=id)
        if not games:
            return 'no permission'
    game.state = GameState.CANCELLED
    game.save()
    return 'success'


@require_permission(*get_attrs(ActionNoId, 'NO005017'))
def get_nodes_by_date_with_time(request, date):
    start = datetime.datetime.combine(date, datetime.time.min)
    end = datetime.datetime.combine(date, datetime.time.max)
    r = utils.get_games()
    r = r.filter(workstarttime__range=(start, end))
    ret = Node.objects.none()
    for i in r:
        ret |= i.game2node.all()
    ret = ret.order_by('deadline')
    return ret