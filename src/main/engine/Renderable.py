import pygame
from abc import ABC, abstractmethod

class Renderable(ABC):
  """
  Interface for objects that can be rendered
  """
  @abstractmethod
  def render(self, displaySurf: pygame.Surface):
    """
    Render the object on the provided Pygame surface

    Args: 
      displaySurf (pygame.Surface): The pygame surface onto which the object should be rendered 
    """
    raise NotImplementedError()