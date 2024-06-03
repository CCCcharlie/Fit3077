from __future__ import annotations
from typing import List


from engine.builder.entity.ButtonBuilder import ButtonBuilder
from engine.command.IncrementCounterCommand import IncrementCounterCommand
from engine.component.CounterComponent import CounterComponent
from engine.component.TransformComponent import TransformComponent
from engine.component.hitbox.RectHitboxComponent import RectHitboxComponent
from engine.component.renderable.RectComponent import RectComponent
from engine.component.renderable.TextComponent import TextComponent
from engine.utils.Vec2 import Vec2
from pygame import Color

from pygame.font import SysFont


from ...command.SetColorCommand import SetColorCommand
from ...command.Command import Command
from ...component.interaction.ButtonComponent import ButtonComponent
from ...component.interaction.ClickableComponent import ClickableComponent
from ...component.hitbox.HitboxComponent import HitboxComponent
from ...component.renderable.RenderableComponent import RenderableComponent
from ...exceptions.IncompleteBuilderError import IncompleteBuilderError
from ...entity.Entity import Entity

class CounterBuilder:
  """
  Build a counter interface
  """
  def __init__(self):
    """
    Initialise the builder
    """
    self.__defaultValue: int = None
    self.__counterText: str = None
    self.__transformComponent: TransformComponent = None

    # internal varaibles
    self.__counter: CounterComponent = None

  def setDefaultValue(self, value: int) -> CounterBuilder:
    self.__defaultValue = value
    return self
  
  def setCounterText(self, text: str) -> CounterBuilder:
    self.__counterText = text
    return self
  
  def setTransformComponent(self, t: TransformComponent) -> CounterBuilder:
    self.__transformComponent = t
    return self 
  
  def getCounter(self) -> CounterComponent:
    return self.__counter
  
  def build(self) -> List[Entity]:
    #checks
    if self.__defaultValue is None:
      raise IncompleteBuilderError(self.__class__.__name__, "Default Value")
    
    if self.__counterText is None:
      raise IncompleteBuilderError(self.__class__.__name__, "Counter Text")
    
    if self.__transformComponent is None:
      raise IncompleteBuilderError(self.__class__.__name__, "Transform Component")


    entities: List[Entity] = []

    baseE = Entity()
    entities.append(baseE)

    # create the background rect
    backgroundRect = RectComponent(self.__transformComponent.clone(), 340, 260, Color(0,0,0))
    baseE.add_renderable(backgroundRect)

    # create the title text
    textTransform: TransformComponent = self.__transformComponent.clone()
    textTransform.position += Vec2(50, 10)
    titleText = TextComponent(self.__transformComponent, self.__counterText)
    baseE.add_renderable(titleText)

    # create the counter display
    counterRectTransform = self.__transformComponent.clone()
    counterRectTransform.position += Vec2(70, 200)
    counterTextRect = RectComponent(counterRectTransform, 200, 50, Color(52,54,69))

    counterTextTransform = counterRectTransform.clone()
    counterTextTransform.position += Vec2(10,0)
    counterText = TextComponent(counterTextTransform, str(self.__defaultValue))

    baseE.add_renderable(counterTextRect)
    baseE.add_renderable(counterText)

    # create the counter component
    counterComponent = CounterComponent(self.__defaultValue, counterText)
    self.__counter = counterComponent # store the counter for return 
    
    # create the decrement button
    incrementCommand = IncrementCounterCommand(counterComponent, -1)
    incrementPosition = self.__transformComponent.clone().position
    incrementPosition += Vec2(10, 200)
    incrementButton = (
      ButtonBuilder()
      .setRectDetails(50,50)
      .setText("-")
      .setPosition(incrementPosition)
      .setOnClick(incrementCommand)
      .build()
    )
    entities.append(incrementButton)

    # create the decrement button
    incrementCommand = IncrementCounterCommand(counterComponent, 1)
    incrementPosition = self.__transformComponent.clone().position
    incrementPosition += Vec2(280, 200)
    incrementButton = (
      ButtonBuilder()
      .setRectDetails(50,50)
      .setText("+")
      .setPosition(incrementPosition)
      .setOnClick(incrementCommand)
      .build()
    )
    entities.append(incrementButton)
    
    return entities

