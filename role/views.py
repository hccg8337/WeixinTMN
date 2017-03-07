from django.shortcuts import render, HttpResponse

import actions


def set_roles(request):
    msg = actions.set_roles()
    return HttpResponse(msg)
