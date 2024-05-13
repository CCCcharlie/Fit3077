from __future__ import annotations
from engine.builder.entity.TextBuilder import TextBuilder
from engine.scene.Scene import Scene


class WinSceneBuilder:
  def __init__(self):
    self.__winningPlayer: int | None = None

  def setWinningPlayer(self, winningPlayer: int) -> WinSceneBuilder:
    self.__winningPlayer = winningPlayer
    return self
  
  def build(self) -> Scene:

    textBuilder = TextBuilder().setText(
      f"Winning player is {self.__winningPlayer}"
    )

    s = Scene()
    s.addEntity(textBuilder.build())
    return s