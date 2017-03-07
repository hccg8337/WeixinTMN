import os
import json

from django.shortcuts import render, HttpResponse

import utils


def read_gamestemplate_config(request):
    error = []
    path = os.path.join('config', 'template', 'games')
    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.conf'):
                r = utils.parse_conf(os.path.join(parent, filename))
                if r:
                    error.append(r)
    if error:
        msg = ','.join(error)
    else:
        msg = 'success'
    return HttpResponse(msg)