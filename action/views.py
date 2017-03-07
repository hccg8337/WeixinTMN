# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

import actions


def set_actions(request):
    msg = actions.set_actions()
    return HttpResponse(msg)
