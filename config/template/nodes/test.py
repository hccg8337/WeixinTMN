import ConfigParser
import re

config = ConfigParser.ConfigParser()
path = ''
try:
    config.read(path)
except Exception:
    pass

ATTR = ['name', 'notifytime', 'comments']

nt_name = config.get('default', 'name')
if not nt_name:
    nt_name = re.split(r'[\\/]+', path)[-1].split('.')[0]
records = list()
ids = set()
old_level = list()
new_level = list()
linked = False
secs = config.sections()
# print(secs)
for i in secs:
    if i == 'default':
        continue
    if i == 'level':
        linked = True
        del old_level[:]
        for j in new_level:
            old_level.append(j)
        # print('newold' + ','.join(new_level))
        del new_level[:]
        # print('old:' + ','.join(old_level))
        # print('new' + ','.join(new_level))
        continue
    record = dict()
    opts = config.options(i)
    record['id'] = i
    ids.add(i)
    # print(i)
    new_level.append(i)
    print(','.join(new_level))
    # print(i + ':' + ','.join(new_level) + ':' + ','.join(old_level))
    for j in ATTR:
        record[j] = config.get(i, j)

    p = list()
    if linked:
        parent = config.get(i, 'parent')
        if parent:
            parent = list(set(parent.split(',')))
            for j in parent:
                for k, val in enumerate(records):
                    if val['id'] == j:
                        p.append(k)
                        break
                    if k > len(records) - len(new_level):
                        break
        else:
            t = len(new_level) - 1 if len(old_level) >= len(new_level) else len(old_level) - 1
            t = old_level[t]
            # print(t)
            for j, val in enumerate(records):
                if val['id'] == t:
                    p.append(j)
                    break
                if j > len(records) - len(new_level):
                    break
    record['type'] = 0
    record['parent'] = p
    records.append(record)
