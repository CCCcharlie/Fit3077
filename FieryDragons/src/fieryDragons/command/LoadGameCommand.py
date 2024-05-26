import random
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.Command import Command
from fieryDragons.Random import Random
from fieryDragons.builder.scene.GameSceneBuilder import GameSceneBuilder
from engine.builder.SceneBuilder import SceneBuilder
from fieryDragons.save.SaveManager import SaveManager


class LoadGameCommand(Command):
  def __init__(self, saveId: int| None = None):
    self.__saveId = saveId
  

  def run(self):
    # load in data
    if self.__saveId is not None:
      SaveManager().load(self.__saveId)

    

    #load game data 
    if self.__saveId is None:
      Random().generateSeed()
    else:
      Random().setSeed(SaveManager().getSeed(self.__saveId))

    #create scene
    gameSceneBuilder = GameSceneBuilder()

    ChangeSceneCommand(gameSceneBuilder).run()

