
from engine.command.Command import Command
from engine.component.CounterComponent import CounterComponent


class IncrementCounterCommand(Command):
  """
  Command to change the value of a counter
  """
  def __init__(self, counterComponent: CounterComponent, amount: int):
    """
    Create the command
    
    Args:
      counterComponent (CounterComponent): the counter to change the value of
      amount (int): The amount to change the counter by 
    """
    self.__counterComponent: CounterComponent = counterComponent
    self.__amount: int = amount

  def run(self):
    """
    Increment the counter
    """
    self.__counterComponent.increment(self.__amount)
    
