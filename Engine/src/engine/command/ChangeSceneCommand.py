from engine.builder.SceneBuilder import SceneBuilder
from engine.command.Command import Command
from engine.scene.World import World


class ChangeSceneCommand(Command):
  """
  Command to change the current active scene
  """
  def __init__(self, newSceneBuilder: SceneBuilder):
    """
    Initialise the change scene command 

    Args:
      newSceneBuilder (SceneBuilder): the builder for the scene to change to 
    """
    self.__newSceneBuilder: SceneBuilder = newSceneBuilder

  def run(self):
    """
    Run the change scene command
    """
    World().setActiveScene(self.__newSceneBuilder.build())