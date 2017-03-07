# -*- coding:utf-8 -*-

import json

from module.models import Module
from models import Action
import utils


@utils.actions_change
def set_actions():
    path = 'config/init/action.json'
    with open(path) as f:
        f = json.load(f)
    not_exists = []
    err_items = []
    ks = f.keys()
    for i in ks:
        r = Module.objects.all().filter(no=i)
        if not r:
            not_exists.append(i)
            continue
        else:
            r = r[0]
            acts = f[i]
            n = 0
            for j in acts:
                n += 1
                if 'no' not in j.keys():
                    err_items.append('%s-%d' % (i, n))
                    continue
                Action.objects.update_or_create(no=j['no'], moduleid=r, defaults=j)
    if not not_exists and not err_items:
        msg = 'set actions success.'
    else:
        msg = ''
        if not_exists:
            msg += 'module no not exist:%s.' % (','.join(not_exists))
        if err_items:
            msg += 'item has error:%s' % (','.join(err_items))
    return msg