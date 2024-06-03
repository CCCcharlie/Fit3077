from __future__ import annotations
from typing import List

from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.builder.entity.CounterBuilder import CounterBuilder
from engine.component.TransformComponent import TransformComponent
from engine.entity.Entity import Entity
from engine.scene.Scene import Scene
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.command.LoadGameCommand import LoadGameCommand
from engine.builder.SceneBuilder import SceneBuilder


class ChooseOptionsSceneBuilder(SceneBuilder):
  def build(self) -> Scene:

    s = Scene() 

    playerCounterTransform: TransformComponent = TransformComponent()
    playerCounterTransform.position = Vec2(World().SCREEN_WIDTH//2 - 170 , 100)
    playerCounterEntities: List[Entity] = (
      CounterBuilder()
      .setDefaultValue(2)
      .setCounterText("Num Players")
      .setTransformComponent(playerCounterTransform)
      .build()
    )

    for e in playerCounterEntities:
      s.addEntity(e)

    segmentsPerCaveTransform: TransformComponent = playerCounterTransform.clone()
    segmentsPerCaveTransform.position += Vec2(0, 300)
    segmentsPerCaveEntities: List[Entity] = (
      CounterBuilder()
      .setDefaultValue(3)
      .setCounterText("Num Segments")
      .setTransformComponent(segmentsPerCaveTransform)
      .build()
    )

    for e in segmentsPerCaveEntities:
      s.addEntity(e)

    # finally add start button
    startButtonTransform = segmentsPerCaveTransform.clone()
    startButtonTransform.position += Vec2(0, 300)
    bb = (
      ButtonBuilder()
      .setRectDetails(300,100)
      .setPosition(startButtonTransform.position)
    )

    # add start button    
    loadGameCommand = LoadGameCommand()
    bb.setOnClick(loadGameCommand)
    bb.setText("Start")
    s.addEntity(bb.build())
    return s 
  
    
  


  

