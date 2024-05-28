
from engine.command.Command import Command


class ShuffleCommand(Command):
  def __init__(self, transforms):
    self.__transforms = transforms


  def run(self):
    print(str(self.__transforms))
    
  