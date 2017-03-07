import json
import datetime

from django.shortcuts import render
from django.forms.models import model_to_dict

from error import Error
from WeixinTMN.models import JsonHttpResponse
from WeixinTMN.utils import require_login, get_session_user
import utils
import actions
from models import MsgStructure


@require_login
def msgslist_for_currentuser(request):
    res = {}
    if request.method == 'GET':
        user = get_session_user(request)
        start = request.GET.get('start', '')
        end = request.GET.get('end', '')
        if start:
            start = datetime.datetime.strptime('%Y%m%d%H%m%', start)
        if end:
            end = datetime.datetime.strptime('%Y%m%d%H%m%', end)
        r = utils.get_msgs_for_user(user, start, end)
        ret = []
        for i in r:
            t = model_to_dict(i)
            t['createtime'] = t['createtime'].strftime('%Y%m%d%H%M%S')
            ret.append(t)
        res['result'] = ret
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))


def set_msg_structures(request):
    actions.set_msg_structures()