import ConfigParser


class ProjectConfig(object):
    pass


def read_config():
    config = ConfigParser.ConfigParser()
    config.read('config.conf')
    secs = config.sections()
    for i in secs:
        if i == 'default':
            continue
        opts = config.options(i)
        for j in opts:
            setattr(ProjectConfig, ('%s_%s' % (i, j)).upper(), config.get(i, j))


read_config()
