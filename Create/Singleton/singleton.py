# -*-encoding:utf-8-*-


# 싱글톤
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(s)

s1 = Singleton()
print(s1)