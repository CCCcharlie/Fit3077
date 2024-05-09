from typing import List

import pygame
from src.main.engine.Entity import Entity
from src.main.engine.Renderable import Renderable
from src.main.engine.Updateable import Updateable


class Scene(Renderable, Updateable):
  def __init__(self):
    """
    Create an empty scene
    """
    self.entities: List[Entity] = []
  
  def addEntity(self, entity: Entity):
    """
    Add an entity to a scene

    Args:
      entity (Entity): The entity to add to the scene
    """
    self.entities.append(entity)

  def update(self, dt: float):
    """
    Update all entities in this scene 

    Args:
      dt (float): fractions of a second to increment by
    """
    for entity in self.entities:
      entity.update(dt)

  def render(self, displaySurf: pygame.Surface):
    """
    Render all the entities in this scene
    
    Args:
      displaySurf (pygame.Surface) surface to render to
    """
    for entity in self.entities:
      entity.render(displaySurf)


  