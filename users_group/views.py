import json

from django.shortcuts import render
from django.forms.models import model_to_dict

from error import Error
from WeixinTMN.models import JsonHttpResponse
from WeixinTMN.utils import require_login
import utils
import actions


@require_login
def usersgroupslist(request):
    res = {}
    if request.method == 'GET':
        r = actions.get_usersgroups(request)
        ret = []
        if not r.err:
            r = r.ret
            for i in r:
                t = model_to_dict(i, fields=['name', 'comments'])
                ret.append(t)
            res['groups'] = ret
        else:
            res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))