from WeixinTMN.utils import require_permission, get_attrs
from action.models import ActionNoId
from models import GamesTemplate


@require_permission(*get_attrs(ActionNoId, 'NO006001'))
def get_gamestemplates(request):
    r = GamesTemplate.objects.all()
    return r