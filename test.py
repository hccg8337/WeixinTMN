# -*- coding:utf-8 -*-

import datetime


"""class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)


class Foo(object):
    __metaclass__ = UpperAttrMetaclass  # 这会作用到这个模块中的所有类
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


print hasattr(Foo, 'bar')
# 输出: False
print hasattr(Foo, 'BAR')
# 输出:True

f = Foo()
print f.BAR
print(dir(f))
"""

print(datetime.datetime.strptime('1000', '%H%M'))