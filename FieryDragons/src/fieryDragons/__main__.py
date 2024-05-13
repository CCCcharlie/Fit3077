from fieryDragons.builder.scene.GameSceneBuilder import GameSceneBuilder
from engine.scene.World import World

if __name__ == "__main__":
    world = World()

    scene = (
        GameSceneBuilder()
        .build()
    )
    world.setActiveScene(scene)
    world.start()
