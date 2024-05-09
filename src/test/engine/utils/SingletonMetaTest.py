##todo create full test


from src.main.engine.utils.SingletonMeta import SingletonMeta

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Example usage
singleton_1 = SingletonClass(10)
singleton_2 = SingletonClass(20)

print(singleton_1.value)  # Output: 10
print(singleton_2.value)  # Output: 10
print(singleton_1 is singleton_2)  # Output: True
