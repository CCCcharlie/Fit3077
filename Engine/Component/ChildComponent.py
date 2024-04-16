from Engine import Entity
from .Component import Component


"""
adds the functionality for entities to have child entities
"""
class ChildComponent(Component):
  def __init__(self, owner: Entity, child: Entity):
    self.owner = owner
    self.child = child


  def update(self):
    self.child.update()

  def render(self, display_surf):
    self.child.render(display_surf)
