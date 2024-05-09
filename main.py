
from src.main.fieryDragons.Builder.Scene.TestSceneBuilder import TestSceneBuilder
from src.main.engine.World import World


if __name__ == "__main__":
  world = World()

  scene = TestSceneBuilder().build()
  world.setActiveScene(scene)
  world.start()

  