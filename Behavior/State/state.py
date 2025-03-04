from abc import abstractmethod, ABCMeta


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB")


class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA")


class Context(State):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def handle(self):
        self.state.handle()


context = Context()
state_A = ConcreteStateA()
state_B = ConcreteStateB()

context.set_state(state_A)
context.handle()

context.set_state(state_B)
context.handle()

