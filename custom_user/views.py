import json

from django.shortcuts import render
from django.forms.models import model_to_dict

from WeixinTMN.utils import require_login
from WeixinTMN.models import JsonHttpResponse
from error import Error
import utils
import actions


@require_login
def userslist(reuqest):
    res = {}
    if reuqest.method == 'GET':
        r = actions.get_users(reuqest)
        if not r.err:
            r = r.ret
            ret = []
            for i in r:
                t = model_to_dict(i, fields=['id', 'nickname'])
                ret.append(t)
            res['users'] = ret
        else:
            res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))