import string
import datetime

from models import MsgState, MsgStateType, Msg, MsgStructure, MsgStructureAction
from node.models import Node
from WeixinTMN.utils import get_session_user, has_permission
from node.utils import get_user_related_to_node, get_users_inchargeof_node
from custom_user.models import CustomUser
from game.models import Game
from game.utils import get_user_related_to_game


def get_msgs_for_user(user, start=None, end=None, startborder=True, endborder=True):
    msgs = MsgState.objects.all().filter(state=MsgStateType.NOTREAD, userid=user)
    r = Msg.objects.all().filter(msgstate2msg__in=msgs)
    if start:
        if startborder:
            r = r.filter(createtime__gte=start)
        else:
            r = r.filter(createtime__gt=start)
    if end:
        if endborder:
            r = r.filter(createtime__lte=end)
        else:
            r = r.filter(createtime__lt=end)
    return r


def update_node_state_msg(func):
    def _deco(*args, **kwargs):
        id = int(args[1]['id'])
        ret = func(*args, **kwargs)
        if ret == 'success':
            n = Node.objects.get(id=id)
            user = get_session_user(args[0])
            ms = MsgStructure.objects.get(no=MsgStructureAction.NODE_STATE_CHANGE)
            t = string.Template(ms.content)
            p = {'1': n.gameid.workstarttime.strftime('%Y-%m-%d %H:%M:%S'),
                 '2': n.gameid.name,
                 '3': n.gameid.place,
                 '4': n.name,
                 '5': n.get_state_display(),
                 '6': user.nickname,
                 '7': args[1]['comments']}
            r = t.safe_substitute(p)
            m = Msg(content=r)
            m.save()
            r = get_user_related_to_node(n)
            for i in r:
                MsgState(msgid=m, userid=i).save()
        return ret
    return _deco


def relate_node_2_user_msg(func):
    def _deco(*args, **kwargs):
        user = get_session_user(args[0])
        n = args[1]
        old_users = get_user_related_to_node(n)
        old = []
        for i in old_users:
            old.append(i.id)
        ret = func(*args, **kwargs)
        if ret == 'success':
            new_users = get_user_related_to_node(n)
            new = []
            new_user_names = []
            for i in new_users:
                new.append(i.id)
                new_user_names.append(i.nickname)
            ms = MsgStructure.objects.get(no=MsgStructureAction.GIVE_NODE_TO_USER)
            adds = [i for i in new if i not in old]
            t = string.Template(ms.content)
            p = {
                '1': n.gameid.workstarttime.strftime('%Y-%m-%d %H:%M:%S'),
                '2': n.gameid.name,
                '3': n.gameid.place,
                '4': n.name,
                '5': n.deadline.strftime('%Y-%m-%d %H:%M:%S') if n.deadline else '',
                '6': user.nickname,
                '7': ','.join(new_user_names),
                '8': n.comments
            }
            r = t.safe_substitute(p)
            m = Msg(content=r)
            m.save()
            for i in adds:
                MsgState(msgid=m, userid=CustomUser.objects.get(id=i)).save()
            ms = MsgStructure.objects.get(no=MsgStructureAction.CANCELL_NODE_FROM_USER)
            cancels = [i for i in old if i not in new]
            t = string.Template(ms.content)
            p = {
                '1': n.gameid.workstarttime.strftime('%Y-%m-%d %H:%M:%S'),
                '2': n.gameid.name,
                '3': n.gameid.place,
                '4': n.name,
                '5': n.deadline.strftime('%Y-%m-%d %H:%M:%S') if n.deadline else '',
                '6': user.nickname,
                '7': ','.join(new_user_names),
                '8': n.comments
            }
            r = t.safe_substitute(p)
            m = Msg(content=r)
            m.save()
            for i in cancels:
                MsgState(msgid=m, userid=CustomUser.objects.get(id=i)).save()
        return ret
    return _deco


def relate_game_to_user_msg(func):
    def _deco(*args, **kwargs):
        ret = func(*args, **kwargs)
        if ret == 'success':
            o = args[1]
            o = Game.objects.get(name=o['name'], workstarttime=o['workstarttime'], workendtime=o['workendtime'])
            ms = MsgStructure.objects.get(no=MsgStructureAction.GIVE_GAME_TO_USER)
            t = string.Template(ms.content)
            users = get_user_related_to_game(o)
            names = []
            for i in users:
                names.append(i.nickname)
            p = {
                '1': o.workstarttime,
                '2': o.name,
                '3': o.place,
                '4': ','.join(names),
                '5': o.comments,
            }
            r = t.safe_substitute(p)
            m = Msg(content=r)
            m.save()
            for i in users:
                MsgState(userid=i, msgid=m).save()
        return ret
    return _deco


def node_overtime_msg(node):
    users = get_users_inchargeof_node(node)
    names = []
    for i in users:
        names.append(i.nickname)
    ms = MsgStructure.objects.get(no=MsgStructureAction.NODE_OVERTIME)
    t = string.Template(ms.content)
    p = {
        '1': datetime.datetime.strptime(node.gameid.workstarttime, '%Y-%m-%d %H:%M:%S'),
        '2': node.gameid.name,
        '3': node.gameid.place,
        '4': node.name,
        '5': datetime.datetime.strptime(node.deadline, '%Y-%m-%d %H:%M:%S'),
        '6': ','.join(names),
    }
    r = t.safe_substitute(p)
    m = Msg(content=r)
    m.save()
    for i in users:
        MsgState(msgid=m, userid=i).save()


def node_notify_msg(node):
    now = datetime.datetime.now()
    if now < node.deadline:
        t = node.deadline - now
        t = t.total_seconds() // 60
    else:
        t = 0
    users = get_users_inchargeof_node(node)
    names = []
    for i in users:
        names.append(i.nickname)
    ms = MsgStructure.objects.get(no=MsgStructureAction.NODE_OVERTIME)
    t = string.Template(ms.content)
    p = {
        '1': datetime.datetime.strptime(node.gameid.workstarttime, '%Y-%m-%d %H:%M:%S'),
        '2': node.gameid.name,
        '3': node.gameid.place,
        '4': node.name,
        '5': datetime.datetime.strptime(node.deadline, '%Y-%m-%d %H:%M:%S'),
        '6': ','.join(names),
        '7': t,
    }
    r = t.safe_substitute(p)
    m = Msg(content=r)
    m.save()
    for i in users:
        MsgState(msgid=m, userid=i).save()