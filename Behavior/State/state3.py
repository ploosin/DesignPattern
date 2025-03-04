# State
class ComputerState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Current: ', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current: ', self, ' => switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name


# ConcreteState
class Off(ComputerState):
    name = "off"
    allowed = ['on']


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


# Context
class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


# Client
if __name__ == '__main__':
    comp = Computer()
    comp.change(On)     # 전원을 켠다
    comp.change(Off)    # 전원을 끈다

    comp.change(On)     # 전원을 켠다
    comp.change(Suspend)    # 일시 중지
    comp.change(Hibernate)  # 절전 모드로 변경할 수 없다
    comp.change(On)     # 전원을 다시 켠다
    comp.change(Off)    # 전원을 끈다
