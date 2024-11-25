
class Qwerty:
    def __init__(self, name, x, y , z):
        self.name = name
        self.x = x
        self.y = y
        self.z = z


def introspection_info(obj):
    ret = {}
    ret['тип'] = type(obj).__name__
    # ret ['класс'] = obj.__class__
    ret['атрибуты'] = [x for x in dir(obj) if not callable(getattr(obj, x))]
    ret['методы'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    if hasattr(obj,'__module__'):
        ret['модуль'] = obj.__module__
    else:
        ret['модуль'] = None

    return ret

object_ = Qwerty('qwer',48,False,[5.2, 15, 6])
print(introspection_info(object_))
print(introspection_info(123))
print(introspection_info(12.3))
print(introspection_info([1,2,3]))
print(introspection_info('123'))
print(introspection_info(True))