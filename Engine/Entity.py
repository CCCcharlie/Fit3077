from abc import ABC, abstractmethod
from typing import List

from Engine import Component 




# https://gameprogrammingpatterns.com/update-method.html

class Entity(ABC): 

  def __init__(self):
    self.components: List[Component] = []


  def add_component(self, component: Component):
    # can you have two of the same component on an object
    # if not then add a check
    self.components.append(component)
    return component


  def get_component(self, component_type):
    for component in self.components:
      if isinstance(component, component_type):
        return component
    return None


  # this method may not live here https://gameprogrammingpatterns.com/component.html
  # as there may be a different better way to do this
  def update(self):
    for component in self.components:
      component.update()
    

  #see above
  def render(self, display_surf):
    for component in self.components:
      component.render(display_surf)
  
    