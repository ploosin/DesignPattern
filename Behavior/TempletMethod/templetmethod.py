from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collect_source(self):
        pass

    @abstractmethod
    def compile_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compile_and_run(self):
        self.collect_source()
        self.compile_to_object()
        self.run()


class Ios_Compiler(Compiler):
    def collect_source(self):
        print("Collecting Swift Source Code")

    def compile_to_object(self):
        print('Compiling Swift code to LLVM bit code')

    def run(self):
        print('Program running on runtime environment')


iOS = Ios_Compiler()
iOS.compile_and_run()



