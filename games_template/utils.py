import ConfigParser
import re
import datetime

from models import GamesTemplate
from game.models import Game, GameType


def get_games_by_gamestemplate(request, gamestemplate):
    r = gamestemplate.gameids.all()
    return r


def parse_conf(path):
    config = ConfigParser.ConfigParser()
    config.read(path)
    ATTR = ['name', 'workstarttime', 'workendtime', 'workextratime', 'place', 'gamestarttime',
            'comments']

    gt_name = config.get('default', 'name')
    gt_comments = config.get('default', 'comments')
    if not gt_name:
        gt_name = re.split(r'[\\/]+', path)[-1].split('.')[0]
    records = list()
    secs = config.sections()
    for i in secs:
        if i == 'default':
            continue
        record = dict()
        opts = config.options(i)
        for j in ATTR:
            if j not in opts:
                return '%s in %s parse error' % (i, gt_name)
            record[j] = config.get(i, j)
        record['type'] = GameType.TEMPLATE
        records.append(record)

    ids = []
    for i in records:
        i['workstarttime'] = datetime.datetime.strptime(i['workstarttime'], '%H%M') if i['workstarttime'] else None
        print(i['workstarttime'])
        i['workendtime'] = datetime.datetime.strptime(i['workendtime'], '%H%M') if i['workendtime'] else None
        print(i['workendtime'])
        i['gamestarttime'] = datetime.datetime.strptime(i['gamestarttime'], '%H%M') if i['gamestarttime'] else None
        print(i['gamestarttime'])
        i['workextratime'] = int(i['workextratime']) if i['workextratime'] else 0
        if not Game.objects.all().filter(name=i['name'], workstarttime=i['workstarttime'], workendtime=i['workendtime']):
            o = Game(**i)
            o.save()
            ids.append(o)

    r, create = GamesTemplate.objects.update_or_create(name=gt_name, defaults={'comments': gt_comments})
    r.gameids = ids