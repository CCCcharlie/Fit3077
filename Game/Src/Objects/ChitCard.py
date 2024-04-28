from Engine import *

from Game.Src.Commands.ChitCardClickedCommand import ChitCardClickedCommand
from Game.Src.Components.ChitCardComponent import ChitCardComponent
from Game.Src.Enums.ChitCardType import ChitCardType


class ChitCard(Entity):
  def __init__(self, x, y, radius, type: ChitCardType, count: int):
    super().__init__()

    colour = (0,0,0)
    if type == ChitCardType.BABY_DRAGON:
      colour = (255,0,255)
    elif type == ChitCardType.BAT:
      colour = (0,0,255)
    elif type == ChitCardType.SALAMANDER:
      colour = (0,255,0)
    elif type == ChitCardType.SPIDER:
     colour = (255,0,0)
    elif type == ChitCardType.PIRATE_DRAGON:
      colour = (0,255,255)

    trans = TransformComponent(self,x,y)
    clickable = ClickableComponent(self,radius*2,radius*2)
    front = CircleComponent(self, radius, colour)
    back = CircleComponent(self, radius, (255,255,255))
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
