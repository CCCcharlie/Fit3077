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
    self.__resetScene: Scene | None = None

  def setWinningPlayer(self, winningPlayer: int) -> WinSceneBuilder:
    self.__winningPlayer = winningPlayer
    return self
  
  def setResetScene(self, b: SceneBuilder) -> WinSceneBuilder:
    self.__resetScene = b.build()
    return self
  
  def build(self) -> Scene:
    s = Scene()

    textBuilder = TextBuilder().setText(
      f"Winning player is {self.__winningPlayer}"
    )
     
    s.addEntity(textBuilder.build())

    bb = ButtonBuilder().setText("Restart").setPosition(Vec2(100,100)).setOnClick(ChangeSceneCommand(self.__resetScene))
    s.addEntity(bb.build())
   
    return s