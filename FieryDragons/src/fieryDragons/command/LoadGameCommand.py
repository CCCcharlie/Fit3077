from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.Command import Command
from engine.Random import Random
from fieryDragons.builder.scene.GameSceneBuilder import GameSceneBuilder
from fieryDragons.save.SaveManager import SaveManager


class LoadGameCommand(Command):
  def __init__(self, saveId):
    self.__saveId = saveId  

  def run(self):
    #load game data 
    Random().setSeed(SaveManager().getSeed(self.__saveId))


    #create scene
    gameSceneBuilder = GameSceneBuilder()
    ChangeSceneCommand(gameSceneBuilder).run()

    # load in data
    SaveManager().load(self.__saveId)


   

