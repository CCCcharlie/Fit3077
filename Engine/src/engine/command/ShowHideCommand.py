
from engine.command.Command import Command
from engine.component.renderable.RenderableComponent import RenderableComponent


class ShowHideCommand(Command):
  """
  Show or hide a renderable component
  """
  def __init__(self, show: bool, renderableComponent: RenderableComponent):
    """
    Create the command
    
    Args:
      show (bool): true = show, false = hide
      renderableComponent (RenderableComponent): The renderable component to show/hide
    """
    self.__show = show
    self.__renderableComponent = renderableComponent

  def run(self):
    """
    Run the show command
    """
    if self.__show:
      self.__renderableComponent.show()
    else:
      self.__renderableComponent.hide()
