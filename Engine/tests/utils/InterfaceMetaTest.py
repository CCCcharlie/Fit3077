
##todo make test class
from engine.utils.InterfaceMeta import InterfaceMeta


class MyInterface(metaclass=InterfaceMeta):
    def method1(self):
        raise NotImplementedError()

    def method2(self):
        raise NotImplementedError()
