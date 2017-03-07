import json

from models import Log
from WeixinTMN.utils import get_session_user
from action.models import ActionNoId, Action
from node.models import Node


def update_node_state_record(func):
    def _deco(*args, **kwargs):
        id = int(args[1]['id'])
        old = Node.objects.get(id=id)
        ret = func(*args, **kwargs)
        if ret == 'success':
            new_state = int(args[1]['state'])
            user = get_session_user(args[0])
            Log(userid=user, objectid=id, actionid=Action.objects.get(id=ActionNoId.NO004013),
                detail=json.dumps({'old': old.state, 'new': new_state, 'comments': args[1]['comments']})).save()
        return ret
    return _deco