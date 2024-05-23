from __future__ import annotations

from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.command.ChangeSceneCommand import ChangeSceneCommand
from engine.command.QuitCommand import QuitCommand
from engine.scene.Scene import Scene
from engine.utils.Vec2 import Vec2
from fieryDragons.Random import Random
from fieryDragons.builder.scene.ChooseSaveSceneBuilder import ChooseSaveSceneBuilder
from fieryDragons.builder.scene.SceneBuilder import SceneBuilder


class MainMenuSceneBuilder(SceneBuilder):
  def build(self) -> Scene:

    Random().setSeed(999)
    
    s = Scene() 

    bb = ButtonBuilder().setRectDetails(150,50)

    # add start button
    bb.setPosition(Vec2(250,100))
    
    nextScene = ChooseSaveSceneBuilder().setResetSceneBuilder(self).build()
    
    bb.setOnClick(ChangeSceneCommand(nextScene))
    bb.setText("Start")
    s.addEntity(bb.build())


     # add quit button
    bb.setPosition(Vec2(250,200))
    bb.setOnClick(QuitCommand())
    bb.setText("Quit")
    s.addEntity(bb.build())
       

    return s 
    
  


  

