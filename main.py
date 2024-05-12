from src.main.fieryDragons.builder.scene.TestChitCardSceneBuilder import TestChitCardSceneBuilder
from src.main.engine.World import World



if __name__ == "__main__":
  world = World()

  scene = TestChitCardSceneBuilder().build()
  world.setActiveScene(scene)
  world.start()

  