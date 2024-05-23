from engine.command.MultiFrameCommand import MultiFrameCommand
from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner


class DelayExecuteMFMFCommand(MultiFrameCommand):
  """
  Executes a MF command after a delay
  """

  def __init__(self, command: MultiFrameCommand, delay: float):
    """
    Create the delay execute command 
    
    Args:
      MFCommand (MultiFrameCommand): The MF command to execute
      delay (float): the delay (in milliseconds) to wait before executing the MF command 
    """
    self.__command: MultiFrameCommand = command
    self.__delay: float = delay

    self.__timeElapsed: float = 0.0

    super().__init__()

  def update(self, dt: float):
    """
    Increment the timer and run the MF command when the timer is done
    """
    self.__timeElapsed += dt

    if self.__timeElapsed > self.__delay:
            #wait time is over
            MultiFrameCommandRunner().addCommand(self.__command)
            self.__command.run()
            self._finish()
            return