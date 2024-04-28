from pygame import Color
from Engine import *
from Game.Src.Components.PlayerPositionComponent import PlayerPositionComponent
from Game.Src.Enums.AnimalType import AnimalType

class Segment(Entity):
  def __init__(self,x, y, animalType: AnimalType):
    super().__init__()


    trans = TransformComponent(self,x,y)
    rect = RectComponent(self, 20,20)
    playerPositionComponent = PlayerPositionComponent(self, animalType)



    if animalType == AnimalType.BABY_DRAGON:
      rect.setColour(Color(255,0,255))
    elif animalType == AnimalType.BAT:
      rect.setColour(Color(0,0,255))
    elif animalType == AnimalType.SALAMANDER:
      rect.setColour(Color(0,255,0))
    elif animalType == AnimalType.SPIDER:
      rect.setColour(Color(255,0,0))


    self.add_component(trans)
    self.add_component(rect)
    self.add_component(playerPositionComponent)