from Engine import *
from Game.Src.Scenes.MainMenuScene import MainMenuScene

if __name__ == "__main__":
  world = World.getInstance()
  scene = MainMenuScene()
  world.setActiveScene(scene)
  world.gameLoop()
