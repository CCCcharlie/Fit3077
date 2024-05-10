from pygame import Color
from main.engine.command.Command import Command
from main.engine.component.renderableComponent.RenderableComponent import RenderableComponent


class SetColorCommand(Command):
  """
  Command to set the color of a renderable component
  """
  def __init__(self, color: Color, renderableComponent: RenderableComponent):
    """
    Create the command
    
    Args:
      color (Color): The color to switch to
      renderableComponent (RenderableComponent): The renderable component to change color of 
    """
    self.__color = color
    self.__renderableComponent = renderableComponent

  def run(self):
    """
    Run the update color command
    """
    self.__renderableComponent.setColor(self.__color)