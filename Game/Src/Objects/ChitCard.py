from pygame import Color
import pygame
from Engine import *

from Game.Src.Commands.ChitCardClickedCommand import ChitCardClickedCommand
from Game.Src.Components.ChitCardComponent import ChitCardComponent
from Game.Src.Enums.ChitCardType import ChitCardType


class ChitCard(Entity):
  def __init__(self, x, y, radius, type: ChitCardType, count: int):
    super().__init__()


    trans = TransformComponent(self,x,y)
    clickable = ClickableComponent(self,radius*2,radius*2)

    front_circle = CircleComponent(self, radius)
    front_text = TextComponent(self, str(count), pygame.font.SysFont("Corbel", 25))
    front_text.setColour(Color(0,0,0))
    front = ComplexSpriteComponent(self, [front_circle,front_text])

    if type == ChitCardType.BABY_DRAGON:
      front_circle.setColour(Color(255,0,255))
    elif type == ChitCardType.BAT:
      front_circle.setColour(Color(0,0,255))
    elif type == ChitCardType.SALAMANDER:
      front_circle.setColour(Color(0,255,0))
    elif type == ChitCardType.SPIDER:
     front_circle.setColour(Color(255,0,0))
    elif type == ChitCardType.PIRATE_DRAGON:
      front_circle.setColour(Color(0,255,255))
    

    back = CircleComponent(self, radius)
    back.setColour(Color(255,255,255))

    circleHitbox = CircleHitboxComponent(self, radius)
    ccComponent = ChitCardComponent(self,front,back)

    chitCardClickCommand = ChitCardClickedCommand(ccComponent)
    button = ButtonComponent(self, chitCardClickCommand)

    commandComponent = CommandComponent(self)

    self.add_component(trans)
    self.add_component(clickable)
    self.add_component(front)
    self.add_component(back)
    self.add_component(ccComponent)
    self.add_component(button)
    self.add_component(commandComponent)
    self.add_component(circleHitbox)
