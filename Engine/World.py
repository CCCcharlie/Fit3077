from typing import List 
import time
import pygame
from pygame.locals import *

from Engine import Entity


# https://gameprogrammingpatterns.com/game-loop.html

class World:
  MS_PER_UPDATE = 16.67  # Assuming 60 frames per second

  def __init__(self):
    pygame.init()
    
    self.size = self.weight, self.height = 640, 400
    self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    self.running = True

    self.background = pygame.Surface(self.display_surf.get_size())
    self.background = self.background.convert()
    self.background.fill((0, 0, 0))

    # how to handle dormant objects https://gameprogrammingpatterns.com/update-method.html#how-are-dormant-objects-handled
    self.entities: List[Entity] = [] # todo use some sort of collection class

  def on_event(self, event):
    if event.type == pygame.QUIT:
      self.running = False

  def on_cleanup(self):
    pygame.quit()

  def getCurrentTime(self):
    return time.time() * 1000  # Convert seconds to milliseconds

  def processInput(self):
    # Placeholder for input processing
    pass

  def update(self):
    for entity in self.entities:
      entity.update()
    
  def render(self):
    # draw black backgorund 
    self.display_surf.blit(self.background, (0,0))

    # add in entity rendering 
    for entity in self.entities:
      entity.render(self.display_surf)
    
    
    pygame.display.flip() # render drawings
  
  def add_entity(self, entity: Entity):
    self.entities.append(entity)

  # much smarted game loop https://gameprogrammingpatterns.com/game-loop.html
  def gameLoop(self):            
    previous = self.getCurrentTime()
    lag = 0.0

    while (self.running):
      for event in pygame.event.get():
        self.on_event(event)

      current = self.getCurrentTime()
      elapsed = current - previous
      previous = current
      lag += elapsed

      self.processInput()

      while lag >= World.MS_PER_UPDATE:
        self.update()
        lag -= World.MS_PER_UPDATE

      self.render()
    self.on_cleanup()





