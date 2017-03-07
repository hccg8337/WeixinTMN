# -*- coding:utf-8 -*-

import json

from django.core.exceptions import ObjectDoesNotExist

from models import JsonHttpResponse
from custom_user.models import SessionUser, CustomUser
from action.models import ActionNoId
from error import Error
from result import Result
from action.utils import get_action_no_id
from role.utils import get_roles


"""def set_models_consts():
    modules = {
        'Game': ['TYPE', 'STATE']
    }
    for i in modules.keys():
        c = eval(i)
        attrs = modules[i]
        for j in attrs:
            cn = type(i + j + 'Const')
            v = getattr(c, j)
            for k in v:
                setattr(cn, k[1].upper(), k[0])
            globals()[i + j + 'Const'] = cn


set_models_consts()"""


def get_session_user(request):
    userid = request.session.get(SessionUser.SESSION_KEY, default='')
    if userid:
        try:
            user = CustomUser.objects.get(id=userid)
            return user
        except ObjectDoesNotExist:
            return
    else:
        return


def require_login(func):
    def _deco(*args, **kwargs):
        req = args[0]
        if get_session_user(req):
            ret = func(*args, **kwargs)
            return ret
        else:
            return JsonHttpResponse(json.dumps({'error': Error.NOTLOGIN}))
    return _deco


def has_permission(user, *actions):
    r1 = user.roles.all().filter(actions__id__in=actions)
    r2 = user.actions.all().filter(id__in=actions)
    return True if r1 or r2 else False


def require_permission(*actions):
    def deco(func):
        def _deco(*args, **kwargs):
            user = get_session_user(args[0])
            if has_permission(user, *actions):
                return Result(ret=func(*args, **kwargs))
            else:
                return Result(err=Error.PERMISSIONDENIED)
        return _deco
    return deco


def get_object_by_attrs_from_old(old, attrs):
    o = {}
    ks = old.keys()
    for i in attrs:
        if i in ks:
            o[i] = old[i]
    return o


def get_attrs(obj, *args, **kwargs):
    r = []
    for i in args:
        d = None
        if i in kwargs.keys():
            d = kwargs[i]
        r.append(getattr(obj, i, d))
    return r