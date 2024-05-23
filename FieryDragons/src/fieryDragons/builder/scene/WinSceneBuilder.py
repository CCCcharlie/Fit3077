from __future__ import annotations
from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.builder.entity.TextBuilder import TextBuilder
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.scene.Scene import Scene
from engine.utils.Vec2 import Vec2
from engine.builder.SceneBuilder import SceneBuilder


class WinSceneBuilder (SceneBuilder):
  def __init__(self):
    self.__winningPlayer: int | None = None

  def setWinningPlayer(self, winningPlayer: int) -> WinSceneBuilder:
    self.__winningPlayer = winningPlayer
    return self
  
  def build(self) -> Scene:
    from fieryDragons.builder.scene.MainMenuSceneBuilder import MainMenuSceneBuilder
    # late import to prevent circular dependency 
    # since Main menu -> Game  -> win screen -> Main menu this creates a circular dependency. 
    #We fix this by late importing in the build stage 

    s = Scene()

    textBuilder = TextBuilder().setText(
      f"Winning player is {self.__winningPlayer}"
    )
     
    s.addEntity(textBuilder.build())

    mainMenuSceneBuilder = MainMenuSceneBuilder()
    changeSceneCommand = ChangeSceneCommand(mainMenuSceneBuilder)
  

    bb = (
      ButtonBuilder()
      .setText("Restart")
      .setPosition(Vec2(100,100))
      .setOnClick(changeSceneCommand)
    )
    s.addEntity(bb.build())
   
    return s