from engine.component.renderable.TextComponent import TextComponent


class CounterComponent:
  def __init__(self, initialValue: int, textComponent: TextComponent):
    self.__value: int = initialValue
    self.__textComponent: TextComponent = textComponent

  def increment(self, amount: int):
    self.__value += amount
    print(f"New value is {self.__value}")
    self.__textComponent.setText(str(self.__value))

  def value(self) -> int:
    print(f"value is {self.__value}")
    return self.__value
