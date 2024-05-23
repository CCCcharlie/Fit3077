from __future__ import annotations
from typing import List

from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from engine.builder.SceneBuilder import SceneBuilder
from fieryDragons.command.LoadGameCommand import LoadGameCommand
from fieryDragons.save.FileDataHandler import FileDataHandler


class ChooseSaveSceneBuilder(SceneBuilder): 
  def build(self) -> Scene:
    s  = Scene()

    pos: Vec2 = Vec2(World().SCREEN_WIDTH/2 - 300 / 2, World().SCREEN_HEIGHT/4)
    bb = (
      ButtonBuilder()
      .setRectDetails(300,100)
      .setPosition(pos)
    )
    
    #load none
    newGame = LoadGameCommand()
    bb.setText("New Game")
    bb.setOnClick(newGame)
    s.addEntity(bb.build())

    saves: List[int] = FileDataHandler().getAllSaves()
    for save in saves:
      loadGame = LoadGameCommand(save)

      # calculate new position
      buttonPos: Vec2 = pos.clone()
      buttonPos.y += 200 * save


      buttonString = f"Load Save {save}"

      bb.setPosition(buttonPos)
      bb.setOnClick(loadGame)
      bb.setText(buttonString)

      s.addEntity(bb.build())
    return s 
    
  


  
