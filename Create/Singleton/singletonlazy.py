# -*-encoding:utf-8-*-


# 싱글톤 - 게으른 초기화
class SingletonLazy:
    __instance = None

    def __init__(self):
        if not SingletonLazy.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created: ", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazy()
        return cls.__instance


s = SingletonLazy()  # 클래스 초기화, 객체 생성 X
print(s)
print("object created", SingletonLazy.get_instance())   # 객체 생성
s1 = SingletonLazy()
s2 = SingletonLazy()
print(s1)
print(s2)

print(s, s1)
