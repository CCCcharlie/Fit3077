from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
import pygame
import time
import sys
from ..utils.Input import Input
from ..scene.Scene import Scene
from ..utils.SingletonMeta import SingletonMeta

class World(metaclass=SingletonMeta):
  """
  The entity that manages the active scene, and the game loop 
  """
  MS_PER_UPDATE: float = 16.67 # 60 update frames per second 
  SCREEN_WIDTH: int = 1920
  SCREEN_HEIGHT: int = 1080

  def __init__(self):
    """
    Create the world

    Setups all pygame things and prepares the game for starting
    """
    pygame.init()
    self.size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    self.display_surf: pygame.Surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    self.background: pygame.Surface = pygame.Surface(self.display_surf.get_size())
    self.background = self.background.convert()
    self.background.fill((220, 209, 235))

    self.activeScene: Scene = None

  
  def setActiveScene(self, scene: Scene):
    """
    Set the active scene 

    Args:
      scene (Scene): THe scene object to set as the new active scene
    """
    if self.activeScene:
      self.activeScene.onCleanup()
    self.activeScene = scene

  def start(self):
    """
    Start the game
    """
    self._gameLoop()
  

  def _on_cleanup(self):
    pygame.quit()

  def _getCurrentTime(self):
    return time.time() * 1000  # Convert seconds to milliseconds
  
  def _render(self):
    # draw background 
    self.display_surf.blit(self.background, (0,0))

    if self.activeScene is not None:
      self.activeScene.render(self.display_surf)
    else:
      print("No active scene")
    
    pygame.display.flip() # render drawings

  # much smarter game loop https://gameprogrammingpatterns.com/game-loop.html
  def _gameLoop(self):            
    previous = self._getCurrentTime()
    lag = 0.0

    while not Input.quitflag:
      
      Input.update()
   
      current = self._getCurrentTime()
      elapsed = current - previous
      previous = current
      lag += elapsed

      # fixed timestep
      while lag >= self.MS_PER_UPDATE:
        self.activeScene.update(self.MS_PER_UPDATE)
        MultiFrameCommandRunner().update(self.MS_PER_UPDATE)
        lag -= self.MS_PER_UPDATE

        

      # render when we can :)
      self._render()
    self._on_cleanup()

    sys.exit()

    

  

