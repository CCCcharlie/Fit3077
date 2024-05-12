class InterfaceMeta(type):
    """
    
    adapted from stack overflow how to define an interface meta class
    """
    def __new__(cls, name, bases, dct):
        if any(isinstance(b, InterfaceMeta) for b in bases):
            return super().__new__(cls, name, bases, dct)
        
        missing_methods = cls.get_missing_methods(name, bases, dct)
        if missing_methods:
            raise TypeError(
                f"Class {name} does not implement the following methods: {', '.join(missing_methods)}"
            )

        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def get_missing_methods(name, bases, dct):
        if "__abstractmethods__" in dct:
            return dct["__abstractmethods__"]
        else:
            missing_methods = set()
            for base in bases:
                if hasattr(base, "__abstractmethods__"):
                    missing_methods.update(base.__abstractmethods__)
            for method in dct:
                if callable(dct[method]) and getattr(dct[method], "__isabstractmethod__", False):
                    missing_methods.add(method)
            return missing_methods


