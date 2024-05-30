import os, sys
from engine.scene.World import World
from fieryDragons.builder.scene.MainMenuSceneBuilder import MainMenuSceneBuilder
from fieryDragons.builder.scene.TestCircularSegmentTrapBuilder import TestCircularSegmentTrapBuilder

try:
    # So assets can be accessed in .exe compiled form
    os.chdir(sys._MEIPASS)
except AttributeError:
    pass

if __name__ == "__main__":
    world = World()
    scene = MainMenuSceneBuilder().build()
    # scene = TestCircularSegmentTrapBuilder().build()
    world.setActiveScene(scene)
    world.start()
