from __future__ import unicode_literals
import urllib

from django.db import models

from conf import ProjectConfig


class WeixinConfig(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.TextField(default='')

    class Meta:
        ordering = ['name']


class WeixinAccountMsg(object):
    APPID = ProjectConfig.WEIXIN_ACCOUNT_APPID
    SECRET = ProjectConfig.WEIXIN_ACCOUNT_SECRET
    TOKEN = ProjectConfig.WEIXIN_ACCOUNT_TOKEN


class WeixinAccessToken(object):
    URL = 'https://api.weixin.qq.com/cgi-bin/token'
    TRY_TIMES = 3
    ACCESS_TOKEN = 'access_token'
    EXPIRES_IN = 'expires_in'
    ACCESS_TOKEN_NAME = ACCESS_TOKEN
    EXPIRES_IN_NAME = '_'.join([ACCESS_TOKEN, EXPIRES_IN])
    PARAMS = {'appid': WeixinAccountMsg.APPID,
              'secret': WeixinAccountMsg.SECRET,
              'grant_type': 'client_credential'}


class WeixinAuth(object):
    URL = ('%s?appid=%s&%s&response_type=code&scope=snsapi_userinfo&state=State&connect_redirect=1#wechat_redirect'
              % ('https://open.weixin.qq.com/connect/oauth2/authorize',
                 WeixinAccountMsg.APPID,
                 urllib.urlencode({'redirect_uri': 'http://%s/weixininterface/authtoindex' % ProjectConfig.HOST_DOMAIN})))


class WeixinMenu(object):
    URL = 'https://api.weixin.qq.com/cgi-bin/menu/create'