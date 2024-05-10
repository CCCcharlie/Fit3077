from abc import ABC, abstractmethod

class Command(ABC):
  """
  Interface for commands

  The command design pattern is used to allow reuse of code via the use of different commands
  """

  @abstractmethod
  def run(self):
    """
    Run the command
    """
    raise NotImplementedError()