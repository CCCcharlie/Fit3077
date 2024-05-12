from typing import List

import pygame

from .Renderable import Renderable
from .Updateable import Updateable

class Entity(Updateable, Renderable): 
  """
  Abstract class representing game objects
  """

  def __init__(self):
    """
    Create an empty Entity
    """
    self.renderables: List[Renderable] = []
    self.updateables: List[Updateable] = []

  def add_renderable(self, renderable: Renderable):
    """
    Add a renderable component to the entity.

    Args:
      renderable (Renderable): The renderable to add.
    """
    self.renderables.append(renderable)

  def add_updateable(self, updateable: Updateable):
    """
    Add an updateable component to the entity.

    Args:
      updateable (Updatable): the updateable to add. 
    """
    self.updateables.append(updateable)

  def update(self, dt: float):
      """
      Update all updateables in this entity

      Args:
        dt (float): fractions of a second to increment by
      """
      for updateable in self.updateables:
         updateable.update(dt)

  def render(self, displaySurf: pygame.Surface):
    """
    Render all the renderables in this entity 

    Args:
      displaySurf (pygame.Surface): surface to render to 
    """
    for renderable in self.renderables:
      renderable.render(displaySurf)


    
