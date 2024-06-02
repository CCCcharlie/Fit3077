from __future__ import annotations
from typing import List, Tuple
from engine.command.DelayExecuteMFCommand import DelayExecuteMFCommand
from engine.command.DelayExecuteMFMFCommand import DelayExecuteMFMFCommand
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.command.SetColorCommand import SetColorCommand
from engine.command.ShowHideCommand import ShowHideCommand
from engine.component.TransformComponent import TransformComponent
from engine.component.hitbox.CircleHitboxComponent import CircleHitboxComponent
from engine.component.hitbox.HitboxComponent import HitboxComponent
from engine.component.interaction.ButtonComponent import ButtonComponent
from engine.component.interaction.ClickableComponent import ClickableComponent
from engine.component.renderable.CircleComponent import CircleComponent
from engine.component.renderable.SpriteComponent import SpriteComponent
from engine.entity.Entity import Entity
from engine.exceptions.IncompleteBuilderError import IncompleteBuilderError
from engine.command.Command import Command
from engine.scene.MultiFrameCommandRunner import MultiFrameCommandRunner
from engine.utils.Vec2 import Vec2
from engine.Random import Random
from fieryDragons.command.ChitCardClickedCommand import ChitCardClickedCommand
from fieryDragons.ChitCard import ChitCard


from fieryDragons.command.MoveActivePlayerCommand import MoveActivePlayerCommand
from fieryDragons.command.NotifyChitCardInPositionCommand import NotifyChitCardInPositionCommand
from fieryDragons.command.ShuffleCommand import ShuffleCommand
from fieryDragons.command.SwapCommand import SwapCommand
from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.save.SaveManager import SaveManager
from pygame import Color

class ChitCardBuilder:
  """
  Build a chit card
  """
  def __init__(self, radius: int, leftHand: TransformComponent):
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
    self.__animate : bool = True
    self.__command : Command = None
    self.__animalType : AnimalType = None
    self.__image : str = None

    self.__transforms: List[Tuple[ TransformComponent, TransformComponent]] = []
    self.__leftHand: TransformComponent = leftHand

    self.__chitCards: List[Tuple[AnimalType, str, Command]] = [
      (AnimalType.SALAMANDER, "chitcard/1Salamander.png",MoveActivePlayerCommand(AnimalType.SALAMANDER, 1) ),
      (AnimalType.SALAMANDER, "chitcard/2Salamander.png", MoveActivePlayerCommand(AnimalType.SALAMANDER, 2)),
      (AnimalType.SALAMANDER, "chitcard/3Salamander.png", MoveActivePlayerCommand(AnimalType.SALAMANDER, 3)),
      (AnimalType.BAT, "chitcard/1Bat.png", MoveActivePlayerCommand(AnimalType.BAT, 1)),
      (AnimalType.BAT, "chitcard/2Bat.png", MoveActivePlayerCommand(AnimalType.BAT, 2)),
      (AnimalType.BAT, "chitcard/3Bat.png", MoveActivePlayerCommand(AnimalType.BAT, 3)),
      (AnimalType.SPIDER, "chitcard/1Spider.png", MoveActivePlayerCommand(AnimalType.SPIDER, 1)),
      (AnimalType.SPIDER,"chitcard/2Spider.png", MoveActivePlayerCommand(AnimalType.SPIDER, 2)),
      (AnimalType.SPIDER, "chitcard/3Spider.png", MoveActivePlayerCommand(AnimalType.SPIDER, 3)),
      (AnimalType.BABY_DRAGON, "chitcard/1BabyDragon.png", MoveActivePlayerCommand(AnimalType.BABY_DRAGON, 1)),
      (AnimalType.BABY_DRAGON, "chitcard/2BabyDragon.png", MoveActivePlayerCommand(AnimalType.BABY_DRAGON, 2)),
      (AnimalType.BABY_DRAGON, "chitcard/3BabyDragon.png", MoveActivePlayerCommand(AnimalType.BABY_DRAGON, 3)),
      (AnimalType.PIRATE_DRAGON, "chitcard/1PirateDragon.png", MoveActivePlayerCommand(AnimalType.PIRATE_DRAGON, 1)),
      (AnimalType.PIRATE_DRAGON, "chitcard/1PirateDragon.png", MoveActivePlayerCommand(AnimalType.PIRATE_DRAGON, 1)),
      (AnimalType.PIRATE_DRAGON, "chitcard/2PirateDragon.png", MoveActivePlayerCommand(AnimalType.PIRATE_DRAGON, 2)),
      (AnimalType.PIRATE_DRAGON, "chitcard/2PirateDragon.png", MoveActivePlayerCommand(AnimalType.PIRATE_DRAGON, 2)),
      (AnimalType.SHUFFLE, "chitcard/Shuffle.png", ShuffleCommand(self.__transforms, self.__leftHand)),
      (AnimalType.SHUFFLE, "chitcard/swapPosition.png", SwapCommand()),
    ]

    self.__numChitCards: int = len(self.__chitCards)

    Random().shuffle(self.__chitCards)

  def onCleanup(self) -> None:
     self.__transforms = []

  def setPosition(self, position: Vec2) -> ChitCardBuilder:
    self.__positionChanged = True
    self.__position = position
    return self

  def setAnimate(self, value : bool) -> ChitCardBuilder:
      self.__animate = value
      return self

  def setImageOverride(self, image : str) -> ChitCardBuilder:
      self.__image = image
      return self

  def setCommandOverride(self, command : Command) -> ChitCardBuilder:
      self.__command = command
      return self

  def setAnimalTypeOverride(self, animalType : AnimalType) -> ChitCardBuilder:
      self.__animalType = animalType
      return self

  def has_more_cards(self) -> bool:
        return len(self.__chitCards) > 0

  def build(self) -> Entity:
    self.__index += 1
    if self.__positionChanged is False:
      raise IncompleteBuilderError("ChitCard", "Position")
    
    if self.__animalType is not None:
        self.__chitCards = list(filter(lambda x : x[0] == self.__animalType, self.__chitCards))
    animalType, imageLocation, command = self.__chitCards.pop()
    if self.__image is not None:
        imageLocation = self.__image
    if self.__command is not None:
        command = self.__command

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

    ccComponent = ChitCard([transformComponent, transform],[front_circle, front_image], back_circle, command)
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

    # move chit cards by 'slamming them down'
    if self.__animate:
      start = TransformComponent()
      start.scale = Vec2(10,10)
      start.position = transformComponent.position
      # start.position = Vec2(World().SCREEN_WIDTH/2, World().SCREEN_HEIGHT/2)
      imageDelayMove = DelayExecuteMFMFCommand(
      LinearMoveMFCommand(
          start,
          transformComponent,
          transformComponent, 
          300
      ),
      self.__index * 250 + 5500
      )
      MultiFrameCommandRunner().addCommand(imageDelayMove)

      imageDelayMove.run()
 
      #hide the chit card
      back_circle.hide()

      #show the chit card once the slam animation begins
      showBackOnSlamCommand = DelayExecuteMFCommand(ShowHideCommand(True, back_circle), self.__index * 250 + 5500)
      MultiFrameCommandRunner().addCommand(showBackOnSlamCommand)
      showBackOnSlamCommand.run()

      # move animals by slamming them down
      start = TransformComponent()
      start.scale = Vec2(10,10)
      start.position = transform.position
      # start.position = Vec2(World().SCREEN_WIDTH/2, World().SCREEN_HEIGHT/2)
      imageDelayMove = DelayExecuteMFMFCommand(
      LinearMoveMFCommand(
          start,
          transform,
          transform, 
          300
      ),
      self.__index * 250 + 5500
      )
      MultiFrameCommandRunner().addCommand(imageDelayMove)
      imageDelayMove.run()

      #finally notify the chit card that it is in position after the slam
      finishCommand = DelayExecuteMFCommand(NotifyChitCardInPositionCommand(ccComponent), 5500 + 250 * (self.__numChitCards + 1))
      MultiFrameCommandRunner().addCommand(finishCommand)
      finishCommand.run()

    self.__transforms.append((transform, transformComponent))

    return e
  





