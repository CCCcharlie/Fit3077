
from typing import List
from engine.command.MultiFrameCommand import MultiFrameCommand
from engine.utils.SingletonMeta import SingletonMeta



class MultiFrameCommandRunner(metaclass=SingletonMeta):
  def __init__(self):
    self.__commands: List[MultiFrameCommand] = []
  
  def addCommand(self, c: MultiFrameCommand):
    self.__commands.append(c)

  def update(self, dt: float):
    # run all commands
    for command in self.__commands:
      if command.isRunning():
        command.update(dt)

    #destroy all finished commands
    newCommands: List[MultiFrameCommand] = []
    for command in self.__commands:
      if command.isFinished() is False:
        newCommands.append(command)

    self.__commands = newCommands
