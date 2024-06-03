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
    numPlayers = SaveManager().getNumPlayers(self.__saveId)
    numSegments = SaveManager().getNumSegments(self.__saveId)


    #create scene
    gameSceneBuilder = (
      GameSceneBuilder()
      .setNumSegmentPerVolcanoCard(numSegments)
      .setNumPlayers(numPlayers)
    )

    ChangeSceneCommand(gameSceneBuilder).run()

    # load in all serialisable data
    SaveManager().load(self.__saveId)


   

