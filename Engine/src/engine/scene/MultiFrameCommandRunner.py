
from typing import List
from engine.command.MultiFrameCommand import MultiFrameCommand
from engine.utils.SingletonMeta import SingletonMeta



class MultiFrameCommandRunner(metaclass=SingletonMeta):
  def __init__(self):
    """
    Create the multiframe command runner
    """
    self.__commands: List[MultiFrameCommand] = []
  
  def addCommand(self, c: MultiFrameCommand):
    """
    Add a command to the multi frame command runner
    
    Args:
      c (MultiFrameCommand): the command to add
    """
    self.__commands.append(c)

  def clear(self):
    """
    Delete all current commands
    """
    self.__commands = []

  def update(self, dt: float):
    """
    Run the update method on all commands and destroy those who are done

    Args:
      dt (float): the time in milliseconds since the last update
    """
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
