# -*-encoding:utf-8-*-


# 상태를 공유
class Borg:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

#
# b = Borg()
# b1 = Borg()
#
# b.x = 4
#
# print('b: ', b)
# print('b1: ', b1)
# print('b dict: ', b.__dict__)
#
# print('b1 dict: ', b1.__dict__)


# __new__를 사용한 Borg
class BorgNew(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(BorgNew, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

#
# b = BorgNew()
# b._shared_state = {'1': '2'}
# b1 = BorgNew()
# print(b, b1)
# print(b.__dict__, b1.__dict__)
#