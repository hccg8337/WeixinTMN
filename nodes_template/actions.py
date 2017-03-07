# -*- coding:utf-8 -*-

import ConfigParser
import re
import datetime

from django.core.exceptions import ObjectDoesNotExist

from error import Error
from WeixinTMN.utils import require_permission, get_attrs
from action.models import ActionNoId
from models import NodesTemplate
from node.models import Node, NodeType, NodeIcon, NodesLine
from document.models import Document


@require_permission(*get_attrs(ActionNoId, 'NO007001'))
def get_nodestemplates(request):
    r = NodesTemplate.objects.all()
    return r


"""def parse_conf(path):
    config = ConfigParser.ConfigParser()
    config.read(path)
    ATTR = ['name', 'notifytime', 'comments']

    nt_name = config.get('default', 'name')
    nt_comments = config.get('default', 'comments')
    if not nt_name:
        nt_name = re.split(r'[\\/]+', path)[-1].split('.')[0]
    records = []
    ids = set()
    old_level = []
    new_level = []
    linked = False
    secs = config.sections()
    for i in secs:
        if i == 'default':
            continue
        if i.startswith('level'):
            linked = True
            del old_level[:]
            for j in new_level:
                old_level.append(j)
            del new_level[:]
            continue
        record = dict()
        opts = config.options(i)
        if i in ids:
            return 'fail'
        record['id'] = i
        ids.add(i)
        new_level.append(i)
        for j in ATTR:
            if j not in opts:
                return '%s in %s parse error' % (i, nt_name)
            record[j] = config.get(i, j)
        p = []
        if linked:
            parent = config.get(i, 'parent')
            if parent:
                parent = list(set(parent.split(',')))
                for j in parent:
                    if j not in ids:
                        return False
                    for k, val in enumerate(records):
                        if val['id'] == j:
                            p.append(k)
                            break
                        if k > len(records) - len(new_level):
                            break
                    if not p:
                        return False
            else:
                t = len(new_level) - 1 if len(old_level) >= len(new_level) else len(old_level) - 1
                t = old_level[t]
                for j, val in enumerate(records):
                    if val['id'] == t:
                        p.append(j)
                        break
                    if j > len(records) - len(new_level):
                        break
        record['type'] = NodeType.TEMPLATE
        record['parent'] = p
        records.append(record)
    nodes = []
    for i in records:
        parent = i.pop('parent')
        if i['notifytime']:
            i['notifytime'] = int(i['notifytime'])
        else:
            i.pop('notifytime')
        i.pop('id')
        node = Node(**i)
        node.save()
        if len(nodes):
            if not parent:
                NodeRelationship(nodeid=node).save()
            for j in parent:
                NodeRelationship(nodeid=node, parentnodeid=nodes[j]).save()
        nodes.append(node)

    r, create = NodesTemplate.objects.update_or_create(name=nt_name, defaults={'comments': nt_comments})
    r.nodeids = nodes"""


@require_permission(*get_attrs(ActionNoId, 'NO007002'))
def add_nodestemplate(request, nodestemplate, nodes, lines, tops):
    name = nodestemplate['name']
    if NodesTemplate.objects.all().filter(name=name):
        return 'name exist'
    nt = NodesTemplate(**nodestemplate)
    ns = {}#保存节点
    ids = set()#保存已有的索引
    for i in nodes:
        id = i.pop('id')
        if id in ids:
            return Error.ARGUEMENTERROR
        if 'deadline' in i.keys():
            if i['deadline']:
                i['deadline'] = datetime.datetime.strptime(i['deadline'], '%Y%m%d%H%M%S')
            else:
                i.pop('deadline')
        if 'notifytime' in i.keys():
            i['notifytime'] = int(i['notifytime'])
        documents = []
        if 'doucuments' in i.keys() and i['documents']:
            i.pop('documents')
            ds = i['documents'].split(',')
            for j in ds:
                j = int(j)
                try:
                    d = Document.objects.get(id=j)
                except ObjectDoesNotExist:
                    return Error.ARGUEMENTERROR
                else:
                    documents.append(d)
        icon = int(i['nodeiconid'])
        try:
            icon = NodeIcon.objects.get(id=icon)
        except ObjectDoesNotExist:
            return Error.ARGUEMENTERROR
        else:
            i['nodeiconid'] = icon
        t = Node(**i)
        t.type = NodeType.TEMPLATE
        t.save()
        t.documents = documents
        ids.add(id)
        ns[id] = t
    ks = ns.keys()
    for i in lines:
        if i['start'] not in ks or i['end'] not in ks:
            return Error.ARGUEMENTERROR
        NodesLine(prevnodeid=ns[i['start']], nextnodeid=ns[i['end']]).save()
    tops = ','.join([ns[i].id for i in tops])
    nt.tops = tops
    nt.save()
    nt.nodeids = [ns[i] for i in ks]