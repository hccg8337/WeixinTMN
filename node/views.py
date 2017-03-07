# -*- coding:utf-8 -*-

import json
import traceback

from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from error import Error
from WeixinTMN.utils import require_login, has_permission, get_session_user
from WeixinTMN.models import JsonHttpResponse
from game.actions import get_game_detail
import actions
import utils
from game.models import Game
from nodes_template.utils import get_nodes_by_nodestemplate
from nodes_template.actions import get_nodestemplates
from node.models import Node, NodeState, NodeType
from custom_user.actions import get_users
from users_group.actions import get_usersgroups
from action.models import ActionNoId


@require_login
def flow_index(request):
    error = ''
    if request.method == 'GET':
        game_id = request.GET.get('gameid')
        try:
            r = Game.objects.get(id=int(game_id))
        except ObjectDoesNotExist:
            error = Error.ARGUEMENTERROR
    else:
        error = Error.METHODERROR
    if error:
        return HttpResponse(error)
    else:
        title = '查看工作流'
        return render_to_response('designer.html', locals())


@require_login
def nodesflow(request):
    res = {}
    if request.method == 'GET':
        game_id = request.GET.get('gameid')
        try:
            game = Game.objects.get(id=game_id)
        except ObjectDoesNotExist:
            res['error'] = Error.ARGUEMENTERROR
        else:
            r = actions.get_flow_by_game(request, game)
            if not r.err:
                r = r.ret
                if isinstance(r, str):
                    res['error'] = r
                else:
                    if r:
                        lines = utils.get_lines_by_nodes(r)
                        ret = []
                        for i in lines:
                            t = model_to_dict(i)
                            ret.append(t)
                        res['line'] = ret
                        ret = []
                        for i in r:
                            t = model_to_dict(i, exclude=['type', 'gameid'])
                            if t['deadline']:
                                t['deadline'] = t['deadline'].strftime('%Y%m%d%H%M%S')
                            ret.append(t)
                        #print(ret)
                        res['instance'] = ret
                        res['top'] = game.tops
                        r = utils.get_nodes_by_user(get_session_user(request))
                        r = r.filter(gameid=game)
                        ns = []
                        for i in r:
                            ns.append(i.id)
                        res['changenode'] = ns
                        res['type'] = NodeType.INSTANCE
                    else:
                        r = get_nodestemplates(request)
                        if not r.err:
                            r = r.ret
                            res['type'] = NodeType.TEMPLATE
                            ret = []
                            for i in r:
                                tt = model_to_dict(i, exclude=['nodeids'])
                                t = get_nodes_by_nodestemplate(i)
                                names = []
                                for j in t:
                                    names.append(j.name)
                                tt['nodes'] = ','.join(names)
                                ret.append(tt)
                            res['template'] = ret
                        else:
                            res['type'] = NodeType.INSTANCE
            else:
                res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


#@csrf_exempt
#@require_login
"""def add_node(request):
    res = {}
    if request.method == 'POST':
        node = request.POST.get('node')
        node = json.loads(node)
        try:
            game = Game.objects.get(id=int(node['gameid']))
        except ObjectDoesNotExist:
            traceback.print_exc()
            res['error'] = Error.ARGUEMENTERROR
        else:
            if not utils.nodes_for_game_can_edited(game):
                res['result'] = 'game has edited'
            r = actions.add_node(request, node, game)
            if not r.err:
                res['result'] = r.ret
            else:
                res['error'] = r.err
            if node['groups'] or node['users']:
                n = Node.objects.get(name=node['name'], gameid=game)
                r = actions.permit_node(request, n, node['groups'], node['users'])
                if not r.err:
                    res['result'] = r.ret
                else:
                    res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))"""


#@csrf_exempt
#@require_login
"""def del_node(request):
    res = {}
    if request.method == 'POST':
        node_id = request.POST.get('nodeid')
        try:
            n = Node.objects.get(id=int(node_id))
        except ObjectDoesNotExist:
            res['error'] = Error.ARGUEMENTERROR
        else:
            r = actions.del_node(request, n)
            if not r.err:
                res['result'] = r.ret
            else:
                res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))"""


@require_login
def node_permits(request):
    res = {}
    if request.method == 'GET':
        node_id = request.GET.get('nodeid')
        try:
            n = Node.objects.get(id=int(node_id))
        except ObjectDoesNotExist:
            res['error'] = Error.ARGUEMENTERROR
        else:
            r = get_users(request)
            users = None
            if not r.err:
                r = r.ret
                users = utils.get_users_with_node(n)
                ids = []
                for i in users:
                    ids.append(i.id)
                ret = []
                for i in r:
                    if has_permission(i, ActionNoId.NO004011, ActionNoId.NO004012, ActionNoId.NO004013):
                        t = model_to_dict(i, fields=['id', 'nickname'])
                        if i.id in ids:
                            t['select'] = 1
                        ret.append(t)
                users = ret
            r = get_usersgroups(request)
            groups = None
            if not r.err:
                groups = utils.get_usersgroups_with_node(n)
                ids = []
                for i in groups:
                    ids.append(i.id)
                r = r.ret
                ret = []
                for i in r:
                    t = model_to_dict(i, fields=['id', 'name'])
                    if i.id in ids:
                        t['select'] = 1
                    ret.append(t)
                groups = ret
            if users:
                res['users'] = users
            if groups:
                res['groups'] = groups
    elif request.method == 'POST':
        node = request.POST.get('node')
        node = json.loads(node)
        try:
            n = Node.objects.get(id=node['id'])
        except ObjectDoesNotExist:
            res['error'] = Error.ARGUEMENTERROR
        else:
            r = actions.permit_node(request, n, node['group'], node['user'])
            if not r.err:
                res['result'] = r.ret
            else:
                res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


@csrf_exempt
@require_login
def node_detail(request):
    res = {}
    if request.method == 'POST':
        node = request.POST.get('node')
        node = json.loads(node)
        try:
            n = Node.objects.get(id=int(node['id']))
        except ObjectDoesNotExist:
            res['error'] = Error.ARGUEMENTERROR
        else:
            r = actions.update_node_detail(request, node)
            #print(r.ret)
            if r.err:
                res['error'] = r.err
            else:
                if node['groups'] or node['users']:
                    r = actions.permit_node(request, n, node['groups'], node['users'])
                    if not r.err:
                        res['result'] = r.ret
                    else:
                        res['error'] = r.err
                else:
                    res['result'] = r.ret
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


@csrf_exempt
@require_login
def node_state(request):
    res = {}
    if request.method == 'POST':
        node = request.POST.get('node')
        node = json.loads(node)
        try:
            Node.objects.get(id=int(node['id']))
        except ObjectDoesNotExist:
            res['error'] = Error.ARGUEMENTERROR
        else:
            r = actions.update_node_state(request, node)
            if not r.err:
                res['result'] = r.ret
            else:
                res['error'] = r.err
    else:
        res['error'] = Error.ARGUEMENTERROR
    return JsonHttpResponse(json.dumps(res))


@require_login
def nodeslist(request):
    res = {}
    if request.method == 'GET':
        gameid = int(request.POST.get('gameid'))
        try:
            game = Game.objects.get(id=gameid)
        except ObjectDoesNotExist:
            res['error'] = Error.ARGUEMENTERROR
        else:
            r = actions.get_nodes_by_game(request, game)
            if not r.err:
                r = r.ret
                if isinstance(r, str):
                    res['error'] = r
                else:
                    ret = []
                    for i in r:
                        t = model_to_dict(i, fields=['name', 'deadline', 'comments', 'state'])
                        ret.append(t)
                    res['result'] = ret
            else:
                res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


def check_node_deadline(request):
    actions.check_node_deadline()
    return HttpResponse('success')


@require_login
def update_flow(request):
    res = {}
    if request.method == 'POST':
        flow = request.POST.get('flow')
        flow = json.loads(flow)
        gameid = flow['gameid']
        try:
            game = Game.object.get(id=int(gameid))
        except ObjectDoesNotExist:
            res['error'] = Error.ARGUEMENTERROR
        else:
            r = actions.update_flow(request, game, flow['nodes'], flow['lines'], flow['tops'])
            if not r.err:
                res['result'] = r.ret
            else:
                res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))