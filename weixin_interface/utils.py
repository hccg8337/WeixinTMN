# -*- coding:utf-8 -*-

import traceback
import json

from httpclient import HttpClient
from models import WeixinConfig, WeixinAccessToken, WeixinMenu, WeixinAccountMsg
from custom_user.models import CustomUser
from config.WeixinConfig.menu import weixin_menu_items


def get_access_token(try_times=0):
    try:
        hc = HttpClient(WeixinAccessToken.URL, 'get', params=WeixinAccessToken.PARAMS)
    except Exception:
        r = traceback.print_exc()
        try_times += 1
        if try_times <= WeixinAccessToken.TRY_TIMES:
            return get_access_token(try_times)
        else:
            return r
    else:
        try:
            args = json.loads(hc.rep)
            WeixinConfig.objects.update_or_create(name=WeixinAccessToken.ACCESS_TOKEN_NAME, defaults={'value': args[WeixinAccessToken.ACCESS_TOKEN]})
            WeixinConfig.objects.update_or_create(name=WeixinAccessToken.EXPIRES_IN_NAME, defaults={'value': args[WeixinAccessToken.EXPIRES_IN]})
        except Exception:
            return traceback.print_exc()
        else:
            return 'get access token success'


def set_menu():
    try:
        header = {'Content-Type': 'application/json', 'encoding': 'utf-8'}
        #print(weixin_menu_items)
        hc = HttpClient(WeixinMenu.URL, 'post', headers=header, params=weixin_menu_items,
                        extend={WeixinAccessToken.ACCESS_TOKEN: WeixinConfig.objects.get(name=WeixinAccessToken.ACCESS_TOKEN_NAME).value})
    except Exception:
        traceback.print_exc()
        return 'fail'
    else:
        args = hc.rep
        args = json.loads(args)
        #print(args)
        try:
            if args['errmsg'] == 'ok':
                return
            else:
                return str(args)
        except Exception:
            traceback.print_exc()
            return 'fail'


def get_user(request):
    code = request.GET.get('code')
    r = CustomUser.objects.all().filter(code=code)
    if r:
        return r[0]
    else:
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token'
        params = {
            'appid': WeixinAccountMsg.APPID,
            'secret': WeixinAccountMsg.SECRET,
            'code': code,
            'grant_type': 'authorization_code',
        }
        hc = HttpClient(url, 'get', params=params)
        args = json.loads(hc.rep)
        if 'errcode' in args.keys():
            return str(json.dumps(args))
        return get_user_info(code, args['access_token'], args['openid'])


def get_user_info(code, access_token, openid):
    url = 'https://api.weixin.qq.com/sns/userinfo'
    params = {
        'access_token': access_token,
        'openid': openid,
        'lang': 'zh_CN',
    }
    hc = HttpClient(url, 'get', params=params)
    args = json.loads(hc.rep)
    #print(args['nickname'])
    if 'errcode' in args.keys():
        return str(json.dumps(args))
    user, create = CustomUser.objects.update_or_create(unionid=args['unionid'], defaults={'openid': args['openid'], 'nickname': args['nickname'], 'code': code})
    return user

