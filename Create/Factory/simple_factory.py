from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print('bhow bhow')


class Cat(Animal):
    def do_say(self):
        print('meow meow')


class ForestFactory(object):
    @staticmethod
    def make_sound(object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    # ff = ForestFactory()
    # animal = input('Which animal should make_sound Dog or Cat?')
    # ff.make_sound(animal)

    ForestFactory().make_sound('Cat')
