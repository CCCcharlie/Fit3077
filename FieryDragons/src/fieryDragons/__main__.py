from fieryDragons.builder.scene.TestSceneBuilder import TestSceneBuilder
from engine.scene.World import World

if __name__ == "__main__":
  world = World()

  scene = TestSceneBuilder().build()
  world.setActiveScene(scene)
  world.start()

  
