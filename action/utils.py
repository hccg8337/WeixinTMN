# -*- coding:utf-8 -*-

from models import Action, ActionNoId


def get_action_no_id():
    r = Action.objects.all()
    if r:
        for i in r:
            setattr(ActionNoId, 'NO' + i.moduleid.no + i.no, i.id)
    #print(dir(ActionNoId))


get_action_no_id()


def actions_change(func):
    def _deco(*args, **kwargs):
        ret = func(*args, **kwargs)
        get_action_no_id()
        return ret
    return _deco