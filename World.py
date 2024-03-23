from typing import List 
from Entity import Entity
import time


# https://gameprogrammingpatterns.com/game-loop.html

class World:
  MS_PER_UPDATE = 16.67  # Assuming 60 frames per second

  def getCurrentTime(self):
      return time.time() * 1000  # Convert seconds to milliseconds

  def processInput(self):
      # Placeholder for input processing
      pass

  def update(self):
      for entity in self.entities:
        entity.update()
      pass

  def render(self):
      # Placeholder for rendering
      pass
  
  def __init__(self):
    self.numEntities = 0
    # how to handle dormant objects https://gameprogrammingpatterns.com/update-method.html#how-are-dormant-objects-handled
    self.entities: List[Entity] = [] # todo use some sort of collection class


  # much smarted game loop https://gameprogrammingpatterns.com/game-loop.html
  def gameLoop(self): 

    previous = self.getCurrentTime()
    lag = 0.0

    while True:
      current = self.getCurrentTime()
      elapsed = current - previous
      previous = current
      lag += elapsed

      self.processInput()

      while lag >= World.MS_PER_UPDATE:
        self.update()
        lag -= World.MS_PER_UPDATE

      self.render()





