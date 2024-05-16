from __future__ import annotations

from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.QuitCommand import QuitCommand
from engine.scene.Scene import Scene
from engine.utils.Vec2 import Vec2
from fieryDragons.builder.scene.GameSceneBuilder import GameSceneBuilder
from fieryDragons.builder.scene.SceneBuilder import SceneBuilder


class MainMenuSceneBuilder(SceneBuilder):
  def build(self) -> Scene:
    s = Scene() 

    bb = ButtonBuilder()

    # add start button
    bb.setPosition(Vec2(250,100))
    
    gameScene = GameSceneBuilder().setResetSceneBuilder(self).build()
    bb.setOnClick(ChangeSceneCommand(gameScene))
    bb.setText("Start")
    s.addEntity(bb.build())


     # add quit button
    bb.setPosition(Vec2(250,200))
    bb.setOnClick(QuitCommand())
    bb.setText("Quit")
    s.addEntity(bb.build())
       

    return s 
    
  


  

