# -*- coding:utf-8 -*-

import json
import urllib
import requests
import traceback


class HttpClient(object):
    TIME_OUT = 5

    def __init__(self, url, method, headers=None, params=None, extend=None):
        self.url = url
        self.headers = headers
        self.params = params
        self.extend = extend
        self.__getattribute__(method)()

    def get(self):
        r = requests.get(self.url, params=self.params, headers=self.headers)
        r.encoding = 'utf-8'
        self.rep = r.text

    def post(self):
        url = self.url
        if self.extend:
            ex = urllib.urlencode(self.extend)
            url += '?' + ex
        params = json.dumps(self.params, ensure_ascii=False)
        r = requests.post(url, data=params, headers=self.headers)
        r.encoding = 'utf-8'
        self.rep = r.text