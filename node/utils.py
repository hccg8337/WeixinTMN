import datetime

from django.core.exceptions import ObjectDoesNotExist

from node.models import Node, NodesLine, NodeState, NodeType
from users_group.models import UsersGroupState
from custom_user.models import CustomUser
from role.models import RoleType, Role
from action.models import ActionNoId
from WeixinTMN.utils import has_permission


def get_lines_by_nodes(nodes):
    r = NodesLine.objects.all().filter(prevnodeid__in=nodes)
    return r


def nodes_for_game_can_edited(game):
    r = game.game2node.all().exclude(state=NodeState.NOUSE)
    for i in r:
        if i.state in [NodeState.DONE, NodeState.BROKEN]:
            return False
    return True


def get_nodes_by_user(user):
    nodes = Node.objects.none()
    nodes |= user.nodes.all().exclude(state=NodeState.NOUSE)
    nodes |= Node.objects.all().filter(type=NodeType.INSTANCE).exclude(state=NodeState.NOUSE).filter(usersgroup2node__in=user.usersgroups.all())
    return nodes


def get_users_with_node(node):
    r = node.user2node.all()
    return r


def get_usersgroups_with_node(node):
    r = node.usersgroup2node.all().filter(state=UsersGroupState.USED)
    return r


def get_user_related_to_node(node):
    r = []
    t = get_users_with_node(node)
    gs = get_usersgroups_with_node(node)
    for i in gs:
        t |= i.user2usersgroup.all()
    us = CustomUser.objects.all()
    for i in us:
        if has_permission(i, ActionNoId.NO004003):
            r.append(i)
        elif has_permission(i, ActionNoId.NO004004):
            if i.games.all().filter(id=node.gameid.id):
                r.append(i)
        elif has_permission(i, ActionNoId.NO004017):
            if t.filter(id=i.id):
                r.append(i)
    return r


def get_users_inchargeof_node(node):
    users = node.gameid.user2game.all().filter(roles__in=[Role.objects.get(id=RoleType.MANAGER)])
    users |= get_user_related_to_node(node)
    users = users.distinct('id')
    return users