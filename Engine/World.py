from typing import List 
import time
import pygame
from pygame.locals import *

from Engine.Input import Input
from Engine.Scene import Scene

# https://gameprogrammingpatterns.com/game-loop.html


# todo make renderer class
# todo make game loop class 

class World:
  MS_PER_UPDATE = 16.67  # Assuming 60 frames per second

  def __init__(self):
    pygame.init()

    
    self.size = self.weight, self.height = 640, 400
    self.display_surf: pygame.Surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    self.background: pygame.Surface = pygame.Surface(self.display_surf.get_size())
    self.background = self.background.convert()
    self.background.fill((0, 0, 0))

    #self.scene: List[Scene] = []
    self.activeScene: Scene = None


  def on_cleanup(self):
    pygame.quit()

  def getCurrentTime(self):
    return time.time() * 1000  # Convert seconds to milliseconds

  def render(self):
    # draw black backgorund 
    self.display_surf.blit(self.background, (0,0))

    if self.activeScene != None:
      self.activeScene.render(self.display_surf)
    else:
      print("No active scene")
    
    pygame.display.flip() # render drawings
  
  def setActiveScene(self, scene: Scene):
    self.activeScene = scene

  # much smarter game loop https://gameprogrammingpatterns.com/game-loop.html
  def gameLoop(self):            
    previous = self.getCurrentTime()
    lag = 0.0

    while not Input.quitflag:
      
      Input.update()
   
      current = self.getCurrentTime()
      elapsed = current - previous
      previous = current
      lag += elapsed

      # fixed timestep
      while lag >= World.MS_PER_UPDATE:
        self.activeScene.update()
        lag -= World.MS_PER_UPDATE

      # render when we can :)
      self.render()
    self.on_cleanup()





