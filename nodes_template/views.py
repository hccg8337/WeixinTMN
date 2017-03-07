import os
import json

from django.shortcuts import render, HttpResponse

from WeixinTMN.utils import require_login
from WeixinTMN.models import JsonHttpResponse
import actions
from error import Error


def read_nodestemplate_config(request):
    pass


@require_login
def add_nodestemplate(request):
    res = {}
    if request.method == 'POST':
        nodestemplate = request.POST.get('nodestemplate')
        nodestemplate = json.loads(nodestemplate)
        r = actions.add_nodestemplate(nodestemplate['nodestemplate'], nodestemplate['nodes'], nodestemplate['lines'], nodestemplate['tops'])
        if not r.err:
            res['result'] = r.ret
        else:
            res['error'] = r.err
    else:
        res['error'] = Error.METHODERROR
    return JsonHttpResponse(json.dumps(res))