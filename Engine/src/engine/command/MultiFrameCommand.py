from ..command.Command import Command
from ..entity.Updateable import Updateable

class MultiFrameCommand(Command, Updateable, ABC):
    """
    Command to update on MultiFrame Movement
    """
    def run(self):
        """
        Run the command
        """
        raise NotImplementedError

    def update(self, dt: float):
        """
        Update the object by the provided delta time increment

        Args:
          dt (float): number of seconds this update must process
        """
        raise NotImplementedError()

    def finish(self):
        """
        Finish the Command
        """
        raise NotImplementedError()
