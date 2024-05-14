from engine.command.Command import Command
from engine.scene.Scene import Scene
from engine.scene.World import World


class ChangeSceneCommand(Command):
  def __init__(self, newScene: Scene):
    self.__newScene= newScene

  def run(self):
    World().setActiveScene(self.__newScene)