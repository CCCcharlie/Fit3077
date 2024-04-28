from Engine import *
from Game.Src.Components.PlayerPositionComponent import PlayerPositionComponent
from Game.Src.Enums.AnimalType import AnimalType

class Segment(Entity):
  def __init__(self,x, y, animalType: AnimalType):
    super().__init__()

    trans = TransformComponent(self,x,y)
    rect = RectComponent(self, 20,20,(255,255,255))
    playerPositionComponent = PlayerPositionComponent(self, animalType)

    self.add_component(trans)
    self.add_component(rect)
    self.add_component(playerPositionComponent)