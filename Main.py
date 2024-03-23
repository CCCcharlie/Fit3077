from Engine import *
import pygame

if __name__ == "__main__":
  world = World()

  world.add_entity(Dragable(100,100,100,50,"TEST"))
  world.add_entity(Button(300,100,100,50,"TEST"))

  # start world up 
  world.gameLoop()
