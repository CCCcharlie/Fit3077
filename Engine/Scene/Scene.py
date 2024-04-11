from typing import List

from Engine import Entity


class Scene:
  def __init__(self):
    # how to handle dormant objects https://gameprogrammingpatterns.com/update-method.html#how-are-dormant-objects-handled
    # todo use some sort of collection class
    self.entities: List[Entity] = []

  def addEntity(self, entity: Entity):
    self.entities.append(entity)

  def update(self):
    for entity in self.entities:
      entity.update()

  def render(self, display_surf):
    for entity in self.entities:
      entity.render(display_surf)


  def reset(self):
    pass
