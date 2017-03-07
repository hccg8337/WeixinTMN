import config.msg.msgstructures
from msg.models import MsgStructure


def set_msg_structures():
    for i in config.msg.msgstructures.MSG_STRUCTURES:
        MsgStructure.objects.update_or_create(no=i[1], defaults={'content': i[0]})