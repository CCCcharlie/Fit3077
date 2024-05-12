from ..command.Command import Command

class PrintCommand(Command):
  """
  Command to print text
  """
  def __init__(self, text: str):
    """
    Create the command
    
    Args:
      text (str): the text to print
    """
    self.__text: str = text

  def run(self):
    """
    Run the print text command
    """
    print(self.__text)
