import random
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.Command import Command
from fieryDragons.Random import Random
from fieryDragons.builder.scene.GameSceneBuilder import GameSceneBuilder
from fieryDragons.builder.scene.SceneBuilder import SceneBuilder
from fieryDragons.save.SaveManager import SaveManager


class LoadGameCommand(Command):
  def __init__(self,resetSceneBuilder: SceneBuilder, saveId: int| None = None):
    self.__saveId = saveId
    self.__resetSceneBuilder = resetSceneBuilder
  

  def run(self):
    seed: int = 0
    #load game data 
    if self.__saveId is None:
      seed = random.randint(1,999999)
    else:
      SaveManager().getSeed(self.__saveId)

    Random().setSeed(seed)

    #create scene
    gameScene = GameSceneBuilder().setResetSceneBuilder(self.__resetSceneBuilder).build()

    ChangeSceneCommand(gameScene).run()
    
    # load in data
    if self.__saveId is not None:
      SaveManager().load(self.__saveId)

