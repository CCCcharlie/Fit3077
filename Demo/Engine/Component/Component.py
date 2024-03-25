from Engine import Entity


class Component:
  def __init__(self, owner):
    self.owner: Entity = owner

  def update(self):
    pass

  def render(self, display_surf):
    pass