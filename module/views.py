import ConfigParser

from django.shortcuts import render
from django.http import HttpResponse

from models import Module
import actions


def set_modules(req):
    actions.set_modules()
    return HttpResponse('set mudules success.')