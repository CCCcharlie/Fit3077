from engine.scene.World import World
from fieryDragons.builder.scene.MainMenuSceneBuilder import MainMenuSceneBuilder

if __name__ == "__main__":
    world = World()
    scene = MainMenuSceneBuilder().build()
    world.setActiveScene(scene)
    world.start()
