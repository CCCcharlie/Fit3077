from abc import ABC, abstractmethod

# https://gameprogrammingpatterns.com/update-method.html

class Entity(ABC): 

  def __init__(self):
    self._x = 0
    self._y = 0


  @abstractmethod
  def update(self): #this method will not live here https://gameprogrammingpatterns.com/component.html
    pass


  @abstractmethod
  def render(self): #see above
    pass
  
    