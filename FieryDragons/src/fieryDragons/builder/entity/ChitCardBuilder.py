from __future__ import annotations
from typing import List, Tuple
from engine.command.DelayExecuteMFMFCommand import DelayExecuteMFMFCommand
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.command.PrintCommand import PrintCommand
from engine.command.SetColorCommand import SetColorCommand
from engine.component.TransformComponent import TransformComponent
from engine.component.hitbox.CircleHitboxComponent import CircleHitboxComponent
from engine.component.hitbox.HitboxComponent import HitboxComponent
from engine.component.interaction.ButtonComponent import ButtonComponent
from engine.component.interaction.ClickableComponent import ClickableComponent
from engine.component.renderable.CircleComponent import CircleComponent
from engine.component.renderable.SpriteComponent import SpriteComponent
from engine.component.renderable.TextComponent import TextComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError
from engine.command.Command import Command
from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
from engine.scene.World import World
from engine.utils.Vec2 import Vec2
from fieryDragons.Random import Random
from fieryDragons.command.ChitCardClickedCommand import ChitCardClickedCommand
from fieryDragons.ChitCard import ChitCard


from fieryDragons.command.MoveActivePlayerCommand import MoveActivePlayerCommand
from fieryDragons.command.ShuffleCommand import ShuffleCommand
from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.save.SaveManager import SaveManager
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
    self.__index = 0
    self.__position: Vec2 = Vec2(0,0)
    self.__radius: int = radius

    self.__frontColor: Color = Color(255,255,255)
    self.__backColor: Color = Color(0,0,0)

    self.__positionChanged: bool = False
    self.__animate = True
    self.__animalType = None
    self.__count = None

    self.__chitCards: List[Tuple[int, AnimalType, str]] = [
      (1, AnimalType.SALAMANDER, "chitcard/1Salamander.png"),
      (2, AnimalType.SALAMANDER, "chitcard/2Salamander.png"),
      (3, AnimalType.SALAMANDER, "chitcard/3Salamander.png"),
      (1, AnimalType.BAT, "chitcard/1Bat.png"),
      (2, AnimalType.BAT, "chitcard/2Bat.png"),
      (3, AnimalType.BAT, "chitcard/3Bat.png"),
      (1, AnimalType.SPIDER, "chitcard/1Spider.png"),
      (2, AnimalType.SPIDER,"chitcard/2Spider.png"),
      (3, AnimalType.SPIDER, "chitcard/3Spider.png"),
      (1, AnimalType.BABY_DRAGON, "chitcard/1BabyDragon.png"),
      (2, AnimalType.BABY_DRAGON, "chitcard/2BabyDragon.png"),
      (3, AnimalType.BABY_DRAGON, "chitcard/3BabyDragon.png"),
      (1, AnimalType.PIRATE_DRAGON, "chitcard/1PirateDragon.png"),
      (1, AnimalType.PIRATE_DRAGON, "chitcard/1PirateDragon.png"),
      (2, AnimalType.PIRATE_DRAGON, "chitcard/2PirateDragon.png"),
      (0, AnimalType.SHUFFLE, "chitcard/2PirateDragon.png"),
      (2, AnimalType.PIRATE_DRAGON, "chitcard/2PirateDragon.png")
    ]

    Random().shuffle(self.__chitCards)


    self.__transforms: List[Tuple[ TransformComponent, TransformComponent]] = []


  def setPosition(self, position: Vec2) -> ChitCardBuilder:
    self.__positionChanged = True
    self.__position = position
    return self

  def setAnimate(self, value : bool) -> ChitCardBuilder:
      self.__animate = value
      return self

  def setAnimalType(self, animalType : AnimalType) -> ChitCardBuilder:
      self.__animalType = animalType
      return self

  def setCount(self, count: int) -> ChitCardBuilder:
      self.__count = count 
      return self

  def has_more_cards(self) -> bool:
        return len(self.__chitCards) > 0

  def build(self) -> Entity:
    self.__index += 1
    if self.__positionChanged is False:
      raise IncompleteBuilderError("ChitCard", "Position")
    
    chitCards = self.__chitCards
    if self.__animalType is not None:
        chitCards = list(filter(lambda x : x[1] == self.__animalType, chitCards))
    if self.__count is not None:
        chitCards = list(filter(lambda x : x[0] == self.__count, chitCards))

    amount, animalType, imageLocation = chitCards.pop()

    #set front colour based on animal type
    self.__frontColor = animalType.get_colour()

    transformComponent: TransformComponent = TransformComponent()
    transformComponent.position = self.__position

    hitbox: HitboxComponent = CircleHitboxComponent(transformComponent, self.__radius, False)
    clickable: ClickableComponent = ClickableComponent(hitbox)

    front_circle = CircleComponent(transformComponent, self.__radius, self.__frontColor)
    #front_text = TextComponent(transformComponent, str(amount))
    transform = transformComponent.clone()
    transform.position = transformComponent.position - Vec2(self.__radius, self.__radius) 
    front_image = SpriteComponent(transform, self.__radius * 2, self.__radius *2 , imageLocation)
   

    back_circle = CircleComponent(transformComponent, self.__radius, self.__backColor)

    if (amount == 0):
      command = ShuffleCommand(self.__transforms)
    else:
      command = MoveActivePlayerCommand(animalType, amount)


    ccComponent = ChitCard([front_circle, front_image], back_circle, command)
    SaveManager().register(ccComponent)

    ccClickedCommand: Command = ChitCardClickedCommand(ccComponent)
    onDefault: Command = SetColorCommand(Color(0,0,0), back_circle)
    onHover: Command = SetColorCommand(Color(51,51,49), back_circle)
    onPressed: Command = SetColorCommand(Color(69,69,67), back_circle)

    button: ButtonComponent = ButtonComponent(clickable, ccClickedCommand, onDefault, onHover, onPressed)


    e = Entity()


    e.add_renderable(back_circle)
    e.add_renderable(front_circle)
    #e.add_renderable(front_text)
    e.add_renderable(hitbox)
    e.add_renderable(front_image)

    e.add_updateable(clickable)
    e.add_updateable(button)
    e.add_updateable(ccComponent)

    if amount == 0:
      e.add_updateable(command)

    if self.__animate:
        # move chit cards by 'slamming them down'
        start = TransformComponent()
        start.scale = Vec2(10,10)
        start.position = transformComponent.position
        # start.position = Vec2(World().SCREEN_WIDTH/2, World().SCREEN_HEIGHT/2)
        imageDelayMove = DelayExecuteMFMFCommand(
        LinearMoveMFCommand(
            start,
            transformComponent.clone(),
            transformComponent, 
            300
        ),
        self.__index * 250 + 5500
        )
        MultiFrameCommandRunner().addCommand(imageDelayMove)
        imageDelayMove.run()
        transformComponent.position = Vec2(-100,-100)


        # move animals by slamming them down
        start = TransformComponent()
        start.scale = Vec2(10,10)
        start.position = transform.position
        # start.position = Vec2(World().SCREEN_WIDTH/2, World().SCREEN_HEIGHT/2)
        imageDelayMove = DelayExecuteMFMFCommand(
        LinearMoveMFCommand(
            start,
            transform.clone(),
            transform, 
            300
        ),
        self.__index * 250 + 5500
        )
        MultiFrameCommandRunner().addCommand(imageDelayMove)
        imageDelayMove.run()
        transform.position = Vec2(-100,-100)


    self.__transforms.append((transform, transformComponent))

    return e
  





