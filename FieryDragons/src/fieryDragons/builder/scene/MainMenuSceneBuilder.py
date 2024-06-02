from __future__ import annotations

from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.QuitCommand import QuitCommand
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.builder.scene.ChooseSaveSceneBuilder import ChooseSaveSceneBuilder
from .TutorialSceneBuilder import TutorialSceneBuilder
from engine.builder.SceneBuilder import SceneBuilder


class MainMenuSceneBuilder(SceneBuilder):
  def build(self) -> Scene:

    s = Scene() 


    pos: Vec2 = Vec2(World().SCREEN_WIDTH/2 - 300 / 2, World().SCREEN_HEIGHT/4)
    bb = (
      ButtonBuilder()
      .setRectDetails(300,100)
      .setPosition(pos)
    )


    # add start button    
    nextSceneBuilder = ChooseSaveSceneBuilder()
    bb.setOnClick(ChangeSceneCommand(nextSceneBuilder))
    bb.setText("Start")
    s.addEntity(bb.build())

    # add tutorial button
    pos.y += 200
    nextSceneBuilder = TutorialSceneBuilder()
    bb.setOnClick(ChangeSceneCommand(nextSceneBuilder))
    bb.setText("Tutorial")
    s.addEntity(bb.build())

    # add quit button
    pos.y += 200
    bb.setPosition(pos)
    bb.setOnClick(QuitCommand())
    bb.setText("Quit")
    s.addEntity(bb.build())
       

    return s 
    
  


  

