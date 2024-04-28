from Engine import *
from Game.Src.Components.PlayerPositionComponent import PlayerPositionComponent
from Game.Src.Enums.AnimalType import AnimalType

class Segment(Entity):
  def __init__(self,x, y, animalType: AnimalType):
    super().__init__()

    colour = (0,0,0)
    if animalType == AnimalType.BABY_DRAGON:
      colour = (255,0,255)
    elif animalType == AnimalType.BAT:
      colour = (0,0,255)
    elif animalType == AnimalType.SALAMANDER:
      colour = (0,255,0)
    elif animalType == AnimalType.SPIDER:
     colour = (255,0,0)

    trans = TransformComponent(self,x,y)
    rect = RectComponent(self, 20,20,colour)
    playerPositionComponent = PlayerPositionComponent(self, animalType)

    self.add_component(trans)
    self.add_component(rect)
    self.add_component(playerPositionComponent)