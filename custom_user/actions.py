from django.core.exceptions import ObjectDoesNotExist

from WeixinTMN.utils import require_permission, get_attrs
from models import CustomUser
from action.models import ActionNoId


@require_permission(*get_attrs(ActionNoId, 'NO001001'))
def get_users(request):
    r = CustomUser.objects.all()
    return r