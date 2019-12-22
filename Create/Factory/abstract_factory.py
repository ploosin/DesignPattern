# -*-encoding:utf-8-*-
from abc import ABCMeta, abstractmethod


# Abstract Factory
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


# Concrete Factory
class IndianPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


# Abstract Product
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


# Another Abstract Product
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, veg_pizza):
        pass


# Concrete Product
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)


# Another Concrete Product
class ChickenPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, ' is served with Chicken on', type(veg_pizza).__name__)


class HamPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, ' is served with Ham on', type(veg_pizza).__name__)


class PizzaStore(object):
    def __init__(self):
        self.factory = None
        self.non_veg_pizza = None
        self.veg_pizza = None
        pass

    def make_pizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.make_pizzas()
