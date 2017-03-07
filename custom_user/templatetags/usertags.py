from django import template
from django.core.exceptions import ObjectDoesNotExist

from custom_user.models import CustomUser
from action.models import ActionNoId
import WeixinTMN.utils


register = template.Library()


@register.filter
def get_user_attr(user_id, attr):
    try:
        r = CustomUser.objects.get(id=int(user_id))
    except ObjectDoesNotExist:
        return
    else:
        return getattr(r, attr, '')


@register.filter
def has_permission(user_id, args):
    try:
        r = CustomUser.objects.get(id=int(user_id))
    except ObjectDoesNotExist:
        return
    else:
        t = []
        args = args.split(',')
        for i in args:
            t.append(getattr(ActionNoId, i))
        return WeixinTMN.utils.has_permission(r, *t)