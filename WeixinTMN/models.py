# -*- coding:utf-8 -*-

import datetime

from django.http import HttpResponse


class JsonHttpResponse(HttpResponse):
    def __init__(self, content=b'', *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        super(self.__class__, self).__init__(content, *args, **kwargs)


class Type(object):
    TEMPLATE = 1
    INSTANCE = 2


class LocalTimezone(datetime.tzinfo):
    """实现北京时间的类"""
    ZERO_TIME_DELTA = datetime.timedelta(0)
    LOCAL_TIME_DELTA = datetime.timedelta(hours=8)  # 本地时区偏差

    def utcoffset(self, dt):
        return self.__class__.LOCAL_TIME_DELTA

    def dst(self, dt):
        return self.__class__.ZERO_TIME_DELTA

    def tzname(self, dt):    #tzname需要返回时区名
        return '+08:00'