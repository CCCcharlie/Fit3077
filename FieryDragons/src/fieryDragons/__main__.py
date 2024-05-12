from fieryDragons.builder.scene.TestChitCardSceneBuilder import TestChitCardSceneBuilder
from engine.scene.World import World

if __name__ == "__main__":
  world = World()

  scene = TestChitCardSceneBuilder().build()
  world.setActiveScene(scene)
  world.start()

  
