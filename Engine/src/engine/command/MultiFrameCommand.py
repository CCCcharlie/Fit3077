
from enum import Enum

from engine.command.Command import Command
from engine.entity.Updateable import Updateable

class State(Enum):
  IDLE = 1
  RUNNING = 2
  FINISHED = 3



class MultiFrameCommand(Command, Updateable):
    """
    Command to update on MultiFrame Movement
    """

    def __init__(self):
        self.__state: State = State.IDLE

    def run(self):
        """
        Run the command
        """
        self.__state = State.RUNNING

    def update(self, dt: float):
        """
        Update the object by the provided delta time increment

        Args:
          dt (float): number of seconds this update must process
        """
        raise NotImplementedError()

    def isRunning(self) -> bool:
        """
        is the command running
        """
        return self.__state == State.RUNNING
    
    def isFinished(self) -> bool:
        """
        Has the command finished running
        """
        return self.__state == State.FINISHED
    
    def _finish(self):
        """
        Register that this command has finished running
        """
        self.__state = State.FINISHED





