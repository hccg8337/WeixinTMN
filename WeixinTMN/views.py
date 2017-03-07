# -*- coding:utf-8 -*-

import sys
import StringIO
import datetime

from django.shortcuts import render, render_to_response
from django.http import HttpResponse

import utils
import module.actions
import action.actions
import role.actions
import msg.actions
import weixin_interface.actions
import weixin_interface.utils


def syncdb(request):
    # 重定向标准输出重定向到内存的字符串缓冲(由StringIO模块提供)
    saveout = sys.stdout
    log_out = StringIO.StringIO()
    sys.stdout = log_out
    # 利用django提供的命令行工具来执行“manage.py syncdb”
    from django.core.management import execute_from_command_line
    execute_from_command_line(["manage.py", "syncdb", "--noinput"])
    # 获得“manage.py syncdb”的执行输出结果，并展示在页面
    result = log_out.getvalue()
    sys.stdout = saveout
    return HttpResponse(result.replace("\n", "<br/>"))


def init(request):
    m = ''
    t = [module.actions.set_modules, action.actions.set_actions, role.actions.set_roles, weixin_interface.utils.get_access_token, msg.actions.set_msg_structures]
    for i in t:
        r = i()
        if r:
            m += r + '\n'
    #m = m.replace('\n', '<br />')
    return HttpResponse(m)


@utils.require_login
def index(request):
    title = '查看比赛'
    total, broken, emergency, msg_notread, msg_all = weixin_interface.actions.get_statistics(utils.get_session_user(request),
                                                                            datetime.datetime.now().date())
    total = '%d%%' % (total * 100)
    msg = '%d/%d' % (msg_notread, msg_all)
    return render_to_response('demo.html', locals())
