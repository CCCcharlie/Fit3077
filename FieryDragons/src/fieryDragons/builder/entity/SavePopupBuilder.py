from __future__ import annotations

from typing import List
from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.component.renderable.RenderableComponent import RenderableComponent
from engine.component.renderable.TextComponent import TextComponent
from engine.entity.Entity import Entity
from engine.utils.Vec2 import Vec2
from engine.builder.SceneBuilder import SceneBuilder
from fieryDragons.command.SaveCommand import SaveCommand
from fieryDragons.command.TogglePopupCommand import ShowSavePopup
from pygame import Color


class SavePopupBuilder:
  def build(self) -> List[Entity]:

    #Add popup box
    popup = Entity()
    trans = TransformComponent()
    trans.position = Vec2(100,350)
    popup_rect = RectComponent(trans, 300, 200, Color(0,0,0))
    textPos = trans.clone()
    textPos.position = textPos.position + Vec2(10,10)
    popup_text = TextComponent(textPos, "Which save?")
    popup.add_renderable(popup_rect)
    popup.add_renderable(popup_text)

    renderables: List[RenderableComponent] = [popup_rect, popup_text]

    #Add 3 save buttons
    saveCommand = SaveCommand(1)
    bb1 =  (
      ButtonBuilder()
      .setText("1")
      .setOnClick(saveCommand)
      .setPosition(Vec2(150,425))
      .setRectDetails(50,50)
    )
    b1 = bb1.build()
    renderables.extend(bb1.getStoredRenderables())
    

    saveCommand = SaveCommand(2)
    bb2 =  (
      ButtonBuilder()
      .setText("2")
      .setOnClick(saveCommand)
      .setPosition(Vec2(225,425))
      .setRectDetails(50,50)
    )
    b2 = bb2.build()
    renderables.extend(bb2.getStoredRenderables())
    

    saveCommand = SaveCommand(3)
    bb3 = (
      ButtonBuilder()
      .setText("3")
      .setOnClick(saveCommand)
      .setPosition(Vec2(300,425))
      .setRectDetails(50,50)
    )
    b3 = bb3.build()
    renderables.extend(bb3.getStoredRenderables())
    

    closePopup = ShowSavePopup(False, renderables, [])
    closePopupButtonBuilder = (
      ButtonBuilder()
      .setText("Close")
      .setOnClick(closePopup)
      .setPosition(Vec2(250, 500))
    )
    closePopupButton = closePopupButtonBuilder.build()
    


    #add save button 
    showPopup = ShowSavePopup(True, renderables,[])
    openPopupBuilder = (
      ButtonBuilder()
      .setText("Save")
      .setOnClick(showPopup)
      .setPosition(Vec2(100,300))
    )
    openPopupE = openPopupBuilder.build()

    showPopup.extendPopop(closePopupButtonBuilder.getStoredRenderables())
    showPopup.extendSave(openPopupBuilder.getStoredRenderables())
    closePopup.extendPopop(closePopupButtonBuilder.getStoredRenderables())
    closePopup.extendSave(openPopupBuilder.getStoredRenderables())


    closePopup.run()

    return [openPopupE, popup, b1,b2,b3,closePopupButton]
    # s.addEntity(saveButtonBuilder.build())


  