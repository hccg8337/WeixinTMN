from WeixinTMN.utils import require_permission, get_attrs
from action.models import ActionNoId
from models import UsersGroup, UsersGroupState


@require_permission(*get_attrs(ActionNoId, 'NO003002'))
def get_usersgroups(request):
    r = UsersGroup.objects.all().filter(state=UsersGroupState.USED)
    return r