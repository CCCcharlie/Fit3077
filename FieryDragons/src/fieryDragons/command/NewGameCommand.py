from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.Command import Command
from engine.Random import Random
from engine.component.CounterComponent import CounterComponent
from fieryDragons.builder.scene.GameSceneBuilder import GameSceneBuilder
from fieryDragons.save.SaveManager import SaveManager


class NewGameCommand(Command):
  def __init__(self, playerCounter: CounterComponent, segmentsCounter: CounterComponent):
    self.__playerCounter: CounterComponent = playerCounter
    self.__segmentsCounter: CounterComponent = segmentsCounter


  def run(self):

    # extract value from counter
    numPlayers: int = self.__playerCounter.value()
    numSegments: int = self.__segmentsCounter.value()

    # save this to the save manager
    SaveManager().setNumPlayers(numPlayers)
    SaveManager().setNumSegments(numSegments)

    Random().generateSeed()

    #create scene
    # print(f"generating scene with {numSegments} segments and {numPlayers} players")
    gameSceneBuilder = (
      GameSceneBuilder()
      .setNumSegmentPerVolcanoCard(numSegments)
      .setNumPlayers(numPlayers)
    )

    ChangeSceneCommand(gameSceneBuilder).run()

   

