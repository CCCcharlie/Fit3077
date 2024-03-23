from Engine import Entity
from .Component import Component

class ButtonComponent(Component):
  def __init__(self, owner: Entity):
    self.owner = owner

  def update(self):
    # do different things based on click state 
    # flip colour on hover
    # darken on press
    # trigger event on click 
    pass