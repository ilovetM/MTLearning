"""
某个类只有一个实例；必须自行创建这个实例；必须向整个系统提供这个实例
"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class MtClass(Singleton):
    a = 1


a = MtClass()
b = MtClass()
print(id(a), id(b))


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


@singleton
class MtFactory:
    r = 2

    def __call__(self, *args, **kwargs):
        print(2)

c = MtFactory()
d = MtFactory()

print(id(c), id(d))