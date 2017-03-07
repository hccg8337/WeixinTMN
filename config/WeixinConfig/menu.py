# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from weixin_interface.models import WeixinAuth


weixin_menu_items = {
    "button": [
        {
            "type": "view",
            "name": "Management",
            "url": WeixinAuth.URL,
        },
    ]
}