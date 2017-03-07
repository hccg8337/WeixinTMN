# -*- coding:utf-8 -*-

import hashlib
import datetime

from django.shortcuts import render_to_response, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from WeixinTMN.utils import get_session_user
import utils
import actions
from custom_user.models import SessionUser
from models import WeixinAccountMsg


def refresh_access_token(request):
    r = utils.get_access_token()
    if not r:
        r = 'success'
    return HttpResponse(r)


def set_menu(request):
    r = utils.set_menu()
    if not r:
        r = 'success'
    return HttpResponse(r)


def auth_to_index(request):
    r = utils.get_user(request)
    #print(r)
    if isinstance(r, str):
        return HttpResponse(r)
    else:
        request.session[SessionUser.SESSION_KEY] = r.id
        title = '查看比赛'
        total, broken, emergency, msg_notread, msg_all = actions.get_statistics(r, datetime.datetime.now().date())
        total = '%d%%' % (total * 100)
        msg = '%d/%d' % (msg_notread, msg_all)
        return render_to_response('demo.html', locals())


@csrf_exempt
def check_signature(request):
    echo_str = request.GET.get('echostr')
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')
    args = [WeixinAccountMsg.TOKEN, timestamp, nonce]
    args.sort()
    tmp_str = "%s%s%s" % tuple(args)
    mysig = hashlib.sha1(tmp_str).hexdigest()
    if mysig == signature:
        print('check signature success')
        return HttpResponse(echo_str)
    else:
        print('check signature fail')
        return HttpResponse('fail')