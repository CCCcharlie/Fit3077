from engine.command.Command import Command
from engine.command.MultiFrameCommand import MultiFrameCommand


class DelayExecuteMFCommand(MultiFrameCommand):
  """
  Executes a command after a delay
  """

  def __init__(self, command: Command, delay: float):
    """
    Create the delay execute command 
    
    Args:
      command (Command): The command to execute
      delay (float): the delay (in milliseconds) to wait before executing the command 
    """
    self.__command: Command = command
    self.__delay: float = delay

    self.__timeElapsed: float = 0.0

    super().__init__()

  def update(self, dt: float):
    """
    Increment the timer and run the command when the timer is done
    """
    self.__timeElapsed += dt

    if self.__timeElapsed > self.__delay:
            #wait time is over
            self.__command.run()
            self._finish()
            return