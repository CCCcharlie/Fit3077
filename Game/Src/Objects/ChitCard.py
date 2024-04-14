from Engine import *

from Game.Src.Commands.ChitCardClickedCommand import ChitCardClickedCommand
from Game.Src.Components.ChitCardComponent import ChitCardComponent


class ChitCard(Entity):
  def __init__(self, x, y, radius):
    super().__init__()

    trans = TransformComponent(self,x,y)
    clickable = ClickableComponent(self,radius*2,radius*2)
    front = CircleComponent(self, radius, (161,44,14))
    back = CircleComponent(self, radius, (161,156,14))
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
