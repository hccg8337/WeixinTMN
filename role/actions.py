import os
import json

from django.core.exceptions import ObjectDoesNotExist

from role.models import Role
from action.models import Action
import utils


@utils.roles_change
def set_roles():
    path = os.path.join('config', 'init', 'role.json')
    with open(path) as f:
        f = json.load(f)
    ks = f.keys()
    err_items = []
    for i in ks:
        role = Role.objects.all().filter(name=i)
        if role:
            role = role[0]
        else:
            role = Role(name=i)
            role.save()
        t = f[i]
        l = []
        for j in t:
            moduleid = j[:3]
            no = j[3:]
            try:
                r = Action.objects.get(moduleid=moduleid, no=no)
            except ObjectDoesNotExist:
                err_items.append('%s-%s' % (i, j))
                continue
            else:
                l.append(r)
        role.actions = l
    if not err_items:
        msg = 'set roles success.'
    else:
        msg = ''
        if err_items:
            msg += 'item has error:%s' % (','.join(err_items))
    return msg