# -*- coding:utf-8 -*-

import datetime
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from error import Error
from WeixinTMN.models import JsonHttpResponse
from WeixinTMN.utils import require_login
from models import Game, GameType
from games_template.models import Date2GamesTemplate, GamesTemplate
from games_template.actions import get_gamestemplates
from games_template.utils import get_games_by_gamestemplate
from nodes_template.models import NodesTemplate
import utils
import actions


@csrf_exempt
@require_login
def gameslist(request):
    if request.method == 'GET':
        dt = request.GET.get('date')
        dt = datetime.datetime.strptime(dt, '%Y%m%d')
        d = dt.date()
        r = actions.get_games_by_date(request, d)
        res = {}
        if not r.err:
            r = r.ret
            if r:
                ret = []
                for i in r:
                    t = model_to_dict(i, fields=['id', 'name', 'workstarttime', 'workendtime', 'workextratime',
                                                 'place', 'gamestarttime', 'comments'])
                    t['state'], t['nodename'] = utils.get_game_state(i)#获取比赛状态
                    t['workstarttime'] = t['workstarttime'].strftime('%Y%m%d%H%M%S')
                    t['workendtime'] = t['workendtime'].strftime('%Y%m%d%H%M%S')
                    t['gamestarttime'] = t['gamestarttime'].strftime('%Y%m%d%H%M%S')
                    ret.append(t)
                res['type'] = GameType.INSTANCE
                res['instance'] = ret
            else:
                try:
                    Date2GamesTemplate.objects.get(date=d)
                    res['type'] = GameType.INSTANCE
                except ObjectDoesNotExist:
                    r = get_gamestemplates(request)
                    #print(r.err)
                    if not r.err:
                        res['type'] = GameType.TEMPLATE
                        r = r.ret
                        ret = []
                        for i in r:
                            tt = model_to_dict(i, fields=['id', 'name', 'comments'])
                            t = get_games_by_gamestemplate(request, i)
                            names = []
                            for j in t:
                                names.append(j.name)
                            tt['games'] = ','.join(names)
                            ret.append(tt)
                        res['template'] = ret
                        #print(res)
                    else:
                        res['type'] = GameType.INSTANCE
        else:
            res['result'] = r.err
        return JsonHttpResponse(json.dumps(res))


@csrf_exempt
@require_login
def select_gamestemplate(request):
    res = {}
    if request.method == 'POST':
        gamestemplate_id = request.POST.get('gamestemplateid')
        date = request.POST.get('date')
        gamestemplate_id = int(gamestemplate_id)
        date = datetime.datetime.strptime(date, '%Y%m%d')
        gt = GamesTemplate.objects.get(id=gamestemplate_id)
        r = actions.select_gamestemplate_for_date(request, date, gt)
        if not r.err:
            res['result'] = r.ret
        else:
            res['result'] = r.err
    else:
        res['result'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


@csrf_exempt
@require_login
def add_game(request):
    res = {}
    if request.method == 'POST':
        game = request.POST.get('game')
        game = json.loads(game)
        if game['name'] and game['workstarttime'] and game['workendtime']:
            r = actions.add_game(request, game)
            if not r.err:
                res['result'] = r.ret
            else:
                res['result'] = r.err
        else:
            res['result'] = Error.ARGUEMENTMISSING
    else:
        res['result'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


@csrf_exempt
@require_login
def game_detail(request):
    res = {}
    if request.method == 'POST':
        game = request.POST.get('game')
        game = json.loads(game)
        try:
            Game.objects.get(id=int(game['id']))
        except ObjectDoesNotExist:
            res['result'] = Error.ARGUEMENTERROR
        else:
            r = actions.update_game_detail(request, game)
            if not r.err:
                res['result'] = r.ret
            else:
                res['result'] = r.err
    else:
        res['result'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


@csrf_exempt
@require_login
def select_nodestemplate(request):
    ret = {}
    if request.method == 'POST':
        nodestemplate_id = request.POST.get('nodestemplateid')
        nodestemplate_id = int(nodestemplate_id)
        game_id = request.POST.get('gameid')
        game_id = int(game_id)
        try:
            nt = NodesTemplate.objects.get(id=nodestemplate_id)
            game = Game.objects.get(id=game_id)
        except ObjectDoesNotExist:
            ret['result'] = Error.ARGUEMENTERROR
        else:
            r = actions.select_nodestemplate_for_game(request, game, nt)
            if not r.err:
                ret['result'] = r.ret
            else:
                ret['result'] = r.err
    else:
        ret['result'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(ret))


def set_game_places(request):
    actions.get_places_from_web()
    return HttpResponse('success')


@csrf_exempt
@require_login
def cancel_game(request):
    res = {}
    if request.method == 'POST':
        game_id = request.POST.get('gameid')
        try:
            r = Game.objects.get(id=int(game_id))
        except ObjectDoesNotExist:
            res['result'] = Error.ARGUEMENTERROR
        else:
            r = actions.cancel_game(request, r)
            if not r.err:
                r = r.ret
            else:
                r = r.err
            res['result'] = r
    else:
        res['result'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


@require_login
def nodestimelist(request):
    res = {}
    if request.method == 'GET':
        date = request.GET.get('date')
        date = datetime.datetime.strptime(date, '%Y%m%d').date()
        r = actions.get_nodes_by_date_with_time(request, date)
        if not r.err:
            r = r.ret
            ret = []
            for i in r:
                t = model_to_dict(i, fields=['name', 'deadline', 'notifytime', 'comments', 'state'])
                t['gamename'] = i.gameid.name
                t['deadline'] = t['deadline'].strftime('%Y%m%d%H%M%S') if t['deadline'] else ''
                ret.append(t)
            res['node'] = ret
        else:
            res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))