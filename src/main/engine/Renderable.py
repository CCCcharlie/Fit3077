import pygame
from main.engine.utils.InterfaceMeta import InterfaceMeta


class Renderable(metaclass=InterfaceMeta):
  """
  Interface for objects that can be rendered
  """
  def render(self, displaySurf: pygame.Surface):
    """
    Render the object on the provided Pygame surface

    Args: 
      displaySurf (pygame.Surface): The pygame surface onto which the object should be rendered 
    """
    raise NotImplementedError()