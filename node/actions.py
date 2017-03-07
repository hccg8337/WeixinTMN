import datetime
import traceback

from django.core.exceptions import ObjectDoesNotExist

from WeixinTMN.utils import require_permission, has_permission,get_session_user, get_object_by_attrs_from_old, get_attrs
from action.models import ActionNoId
from node.models import Node, NodeType, NodeState, NodesLine, NodeIcon
from game.models import Game, GameType, GameState
from custom_user.models import CustomUser
from users_group.models import UsersGroup
from error import Error
from document.models import Document
import utils
import log.utils
import msg.utils


@require_permission(*get_attrs(ActionNoId, 'NO004003', 'NO004004', 'NO004017'))
def get_flow_by_game(request, game):
    user = get_session_user(request)
    if has_permission(user, ActionNoId.NO004003):
        pass
    elif has_permission(user, ActionNoId.NO004004):
        user = get_session_user(request)
        games = user.games.all().filter(id=game.id)
        if not games:
            return 'no permission'
    else:
        pass
    r = Node.objects.all().filter(gameid=game).exclude(state=NodeState.NOUSE)
    return r


@require_permission(*get_attrs(ActionNoId, 'NO004001', 'NO004002'))
def add_node(request, node, game):
    """user = get_session_user(request)
    if has_permission(user, ActionNoId.NO004001):
        pass
    else:
        games = user.games.all().filter(id=game.id)
        if not games:
            return Error.PERMISSIONDENIED
    leftnode = int(node['left'])
    #print(leftnode)
    if leftnode:
        try:
            leftnode = Node.objects.get(id=leftnode)
        except ObjectDoesNotExist:
            traceback.print_exc()
            return Error.ARGUEMENTERROR
    else:
        leftnode = None
    t = node['prev']
    #print(t)
    prevnodes = []
    if t:
        t = t.split(',')
        t = list(set(t))
        for i in t:
            i = int(i)
            if i:
                try:
                    prevnodes.append(Node.objects.get(id=i))
                except ObjectDoesNotExist:
                    traceback.print_exc()
                    return Error.ARGUEMENTERROR
    t = node['next']
    #print(t)
    nextnodes = []
    if t:
        t = node['next'].split(',')
        t = list(set(t))
        for i in t:
            i = int(i)
            if i:
                try:
                    nextnodes.append(Node.objects.get(id=i))
                except ObjectDoesNotExist:
                    traceback.print_exc()
                    return Error.ARGUEMENTERROR
    attrs = ['name', 'deadline', 'notifytime', 'comments']
    if not node['name'] or Node.objects.filter(name=node['name'], gameid=game):
        return 'name exist'
    n = get_object_by_attrs_from_old(node, attrs)
    n['type'] = NodeType.INSTANCE
    n['gameid'] = game
    if 'deadline' in n.keys():
        if n['deadline']:
            n['deadline'] = datetime.datetime.combine(game.workstarttime.date(), datetime.datetime.strptime(n['deadline'], '%H%M%S').time())
        else:
            n.pop('deadline')
    n = Node(**n)
    n.save()
    if leftnode:
        if prevnodes:
            r = NodeRelationship.objects.all().filter(nodeid=leftnode)
            if len(r) > 1:
                NodeRelationship.objects.all().filter(nodeid=leftnode, parentnodeid=prevnodes[0]).delete()
            r = NodeRelationship.objects.all().filter(parentnodeid=leftnode)
            if r:
                if nextnodes:
                    next = nextnodes[0]
                    if len(r) > 1:
                        NodeRelationship.objects.all().filter(nodeid=next).update(parentnodeid=n)
                    else:
                        NodeRelationship(nodeid=next, parentnodeid=n).save()
    else:
        if prevnodes:
            NodeRelationship.objects.all().filter(parentnodeid__in=prevnodes).update(parentnodeid=n)
    if prevnodes:
        t = []
        for i in prevnodes:
            t.append(NodeRelationship(nodeid=n, parentnodeid=i))
            NodeRelationship.objects.bulk_create(t)
    return 'success'"""
    pass


@require_permission(*get_attrs(ActionNoId, 'NO004027', 'NO004028', 'NO004029'))
def node2group(request, node, groups):
    user = get_session_user(request)
    if has_permission(user, ActionNoId.NO004027):
        pass
    elif has_permission(user, ActionNoId.NO004028):
        games = user.games.all().filter(id=node.gameid.id)
        if not games:
            return 'no permission'
    else:
        nodes = utils.get_nodes_by_user(user)
        nodes = nodes.filter(id=node.id)
        if not nodes:
            return 'no permission'
    t = []
    for i in groups:
        i = int(i)
        try:
            g = UsersGroup.objects.get(id=i)
        except ObjectDoesNotExist:
            continue
        else:
            t.append(g)
    node.usersgroup2node = t
    return 'success'


@require_permission(*get_attrs(ActionNoId, 'NO004018', 'NO004019', 'NO004020'))
def node2user(request, node, users):
    user = get_session_user(request)
    if has_permission(user, ActionNoId.NO004018):
        pass
    elif has_permission(user, ActionNoId.NO004019):
        games = user.games.all().filter(id=node.gameid.id)
        if not games:
            return 'no permission'
    else:
        nodes = utils.get_nodes_by_user(user)
        nodes = nodes.filter(id=node.id)
        if not nodes:
            return 'no permission'
    t = []
    #print('users')
    #print(users)
    for i in users:
        i = int(i)
        try:
            u = CustomUser.objects.get(id=i)
        except ObjectDoesNotExist:
            continue
        else:
            t.append(u)
    node.user2node = t
    return 'success'


@require_permission(*get_attrs(ActionNoId, 'NO004014', 'NO004015', 'NO004016'))
def del_node(request, node):
    """user = get_session_user(request)
    if has_permission(user, ActionNoId.NO004014):
        pass
    elif has_permission(user, ActionNoId.NO004015):
        games = user.games.all().filter(id=node.gameid.id)
        if not games:
            return 'no permission'
    else:
        nodes = utils.get_nodes_by_user(user)
        nodes = nodes.filter(id=node.id)
        if not nodes:
            return 'no permission'
    node.state = NodeState.NOUSE
    node.save()
    NodeRelationship.objects.all().filter(nodeid=node).delete()
    NodeRelationship.objects.all().filter(parentnodeid=node).delete()
    return 'success'"""
    pass


@require_permission(*get_attrs(ActionNoId, 'NO004008', 'NO004009', 'NO004010'))
def update_node_detail(request, node):
    user = get_session_user(request)
    n = Node.objects.get(id=int(node['id']))
    if has_permission(user, ActionNoId.NO004008):
        pass
    elif has_permission(user, ActionNoId.NO004009):
        games = user.games.all().filter(id=n.gameid.id)
        if not games:
            return 'no permission'
    else:
        nodes = utils.get_nodes_by_user(user)
        nodes = nodes.filter(id=n.id)
        if not nodes:
            return 'no permission'
    if Node.objects.all().filter(name=node['name'], gameid=n.gameid).exclude(id=n.id):
        return 'name exist'
    node.pop('id')
    node.pop('gameid')
    #print(123)
    #print('deadline=%s' % node['deadline'])
    if 'deadline' in node.keys():
        #print(node['deadline'])
        if node['deadline']:
            node['deadline'] = datetime.datetime.combine(n.gameid.workstarttime.date(), datetime.datetime.strptime(node['deadline'], '%H%M%S').time())
        else:
            node.pop('deadline')
    for i in node.keys():
        #print(i)
        setattr(n, i, node[i])
    n.save()
    return 'success'


@require_permission(*get_attrs(ActionNoId, 'NO004011', 'NO004012', 'NO004013'))
@msg.utils.update_node_state_msg
@log.utils.update_node_state_record
def update_node_state(request, node):
    user = get_session_user(request)
    n = Node.objects.get(id=int(node['id']))
    if has_permission(user, ActionNoId.NO004011):
        pass
    elif has_permission(user, ActionNoId.NO004012):
        games = user.games.all().filter(id=n.gameid.id)
        if not games:
            return 'no permission'
    else:
        nodes = utils.get_nodes_by_user(user)
        nodes = nodes.filter(id=n.id)
        if not nodes:
            return 'no permission'
    n.state = int(node['state'])
    n.save()
    return 'success'


@require_permission(*get_attrs(ActionNoId, 'NO004003', 'NO004004', 'NO004017'))
def get_nodes_by_game(request, game):
    r = Node.objects.all().filter(gameid=game).exclude(state=NodeState.NOUSE)
    user = get_session_user(request)
    if has_permission(user, ActionNoId.NO004003):
        pass
    elif has_permission(user, ActionNoId.NO0040004):
        games = user.games.all().filter(id=game.id)
        if not games:
            return 'no permission'
    else:
        r = utils.get_nodes_by_user(user)
    return r


@require_permission(*get_attrs(ActionNoId, 'NO004027', 'NO004028', 'NO004029', 'NO004018', 'NO004019', 'NO004020'))
@msg.utils.relate_node_2_user_msg
def permit_node(request, node, groups, users):
    r = node2group(request, node, groups)
    if r.err:
        return r.err
    else:
        r = node2user(request, node, users)
        if not r.err:
            return r.ret
        else:
            return r.err


def check_node_deadline():
    now = datetime.datetime.now()
    start = datetime.datetime.combine(now.date(), datetime.time.min)
    end = datetime.datetime.combine(now.date(), datetime.time.max)
    games = Game.objects.all().filter(workstarttime__range=(start, end), state=GameState.DEFAULT, type=GameType.INSTANCE)
    for i in games:
        nodes = Node.objects.all().filter(gameid=i).exclude(state=NodeState.NOUSE)
        for j in nodes:
            if j.deadline:
                if j.deadline < now:
                    msg.utils.node_overtime_msg(j)
                elif j.notifytime:
                    if j.deadline < (now + datetime.timedelta(minutes=j.notifytime)):
                        msg.utils.node_notify_msg(j)


@require_permission
def update_flow(request, game, nodes, lines, tops):
    old_nodes = game.game2node.all().exclude(state=NodeState.NOUSE)
    old = {}
    new = {}
    for i in old_nodes:
        old[str(i.id)] = i
    for i in nodes:
        id = i.pop('id')
        if not id.startswith('n'):
            old.pop(id)
        else:
            if 'deadline' in i.keys():
                if i['deadline']:
                    i['deadline'] = datetime.datetime.strptime(i['deadline'], '%Y%m%d%H%M%S')
                else:
                    i.pop('deadline')
            if 'notifytime' in i.keys():
                i['notifytime'] = int(i['notifytime'])
            documents = []
            if 'doucuments' in i.keys() and i['documents']:
                i.pop('documents')
                ds = i['documents'].split(',')
                for j in ds:
                    j = int(j)
                    d = Document.objects.get(id=j)
                    documents.append(d)
            icon = int(i['nodeiconid'])
            icon = NodeIcon.objects.get(id=icon)
            i['nodeiconid'] = icon
            t = Node(**i)
            t.type = NodeType.TEMPLATE
            t.save()
            t.documents = documents
            new[id] = t
    for i in old:
        i.state = NodeState.NOUSE
        i.save()
    old_lines = utils.get_lines_by_nodes(old_nodes)
    old2 = {}
    for i in old_lines:
        old2[str(i.id)] = i
    for i in lines:
        id = i.pop('id')
        if not id.startswith('n'):
            old2.pop(id)
        else:
            start = i['start']
            if start.startswith('n'):
                start = new[start]
            else:
                start = old[start]
            end = i['end']
            if end.startswith('n'):
                end = new[end]
            else:
                end = old[end]
            NodesLine(prevnodeid=start, nextnodeid=end).save()
    for i in old2:
        i.delete()
    tops = tops.split(',')
    tops = [new[i] if i.startswith('n') else i for i in tops]
    game.tops = tops
    game.save()
    return 'success'