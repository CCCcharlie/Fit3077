from __future__ import annotations
from engine.command.SetColorCommand import SetColorCommand
from engine.component.TransformComponent import TransformComponent
from engine.component.hitbox.CircleHitboxComponent import CircleHitboxComponent
from engine.component.hitbox.HitboxComponent import HitboxComponent
from engine.component.interaction.ButtonComponent import ButtonComponent
from engine.component.interaction.ClickableComponent import ClickableComponent
from engine.component.renderable.CircleComponent import CircleComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError
from engine.command.Command import Command
from engine.utils.Vec2 import Vec2
from fieryDragons.command.ChitCardClickedCommand import ChitCardClickedCommand
from fieryDragons.ChitCard import ChitCard


from fieryDragons.enums.AnimalType import AnimalType
from pygame import Color

class ChitCardBuilder:
  """
  Build a chit card
  """
  def __init__(self, radius: int):
    """
    Create the builder 

    Args:
      radius (int): The radius of the chit card 
    """
    self.__position: Vec2 = Vec2(0,0)
    self.__radius: int = radius

    self.__frontColor: Color = Color(255,255,255)
    self.__backColor: Color = Color(0,0,0)

    self.__positionChanged: bool = False

    self.__animalType: AnimalType = None
    self.__amount: int = None

  def setPosition(self, position: Vec2) -> ChitCardBuilder:
    self.__positionChanged = True
    self.__position = position
    return self

  def setAnimalType(self, animalType: AnimalType) -> ChitCardBuilder:
    self.__animalType = animalType
    return self
  
  def setAmount(self, amount: int) -> ChitCardBuilder:
    self.__amount = amount
    return self

  def build(self) -> Entity:
    if self.__positionChanged is False:
      raise IncompleteBuilderError("ChitCard", "Position")

    transformComponent: TransformComponent = TransformComponent()
    transformComponent.position = self.__position

    hitbox: HitboxComponent = CircleHitboxComponent(transformComponent, self.__radius, True)
    clickable: ClickableComponent = ClickableComponent(hitbox)

    front_circle = CircleComponent(transformComponent, self.__radius, self.__frontColor )
    back_circle = CircleComponent(transformComponent, self.__radius, self.__backColor)

    ccComponent = ChitCard(front_circle, back_circle, self.__animalType, self.__amount)
    
    ccClickedCommand: Command = ChitCardClickedCommand(ccComponent)
    onDefault: Command = SetColorCommand(Color(0,0,0), back_circle)
    onHover: Command = SetColorCommand(Color(0,0,255), back_circle)
    onPressed: Command = SetColorCommand(Color(0,255,0), back_circle)

    button: ButtonComponent = ButtonComponent(clickable, ccClickedCommand, onDefault, onHover, onPressed)


    e = Entity()

    e.add_renderable(front_circle)
    e.add_renderable(back_circle)
    e.add_renderable(hitbox)

    e.add_updateable(clickable)
    e.add_updateable(button)

    return e




