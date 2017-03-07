import ConfigParser

from models import Module


def set_modules():
    path = 'config/init/module.conf'
    config = ConfigParser.ConfigParser()
    config.read(path)

    secs = config.sections()
    for i in secs:
        r = Module.objects.all().filter(no=i)
        if r:
            opts = config.options(i)
            t = {}
            for j in opts:
                t[j] = config.get(i, j)
            r.update(**t)
        else:
            t = {'no': i}
            opts = config.options(i)
            for j in opts:
                t[j] = config.get(i, j)
            Module(**t).save()