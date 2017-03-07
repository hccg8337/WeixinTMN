from models import Role, RoleType


def get_roles():
    r = Role.objects.all()
    for i in r:
        setattr(RoleType, i.name.upper(), i.id)


get_roles()


def roles_change(func):
    def _deco(*args, **kwargs):
        ret = func(*args, **kwargs)
        get_roles()
        return ret
    return _deco