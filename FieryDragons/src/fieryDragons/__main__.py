from fieryDragons.builder.scene.GameSceneBuilder import GameSceneBuilder
from engine.scene.World import World

if __name__ == "__main__":
  world = World()

  scene = GameSceneBuilder(world.size[0], world.size[1],).setPlayers(4).setSegments(16).setChitCards(24).build()
  world.setActiveScene(scene)
  world.start()

  
