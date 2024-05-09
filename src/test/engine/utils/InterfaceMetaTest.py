from main.engine.utils.InterfaceMeta import InterfaceMeta

##todo make test class
class MyInterface(metaclass=InterfaceMeta):
    def method1(self):
        raise NotImplementedError()

    def method2(self):
        raise NotImplementedError()