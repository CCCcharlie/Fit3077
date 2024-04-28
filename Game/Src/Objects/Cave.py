from pygame import Color
from Engine import *

from Game.Src.Components.PlayerPositionComponent import PlayerPositionComponent
from Game.Src.Enums.AnimalType import AnimalType

class Cave(Entity):
  def __init__(self, x, y, animalType: AnimalType):
    super().__init__()

    trans = TransformComponent(self,x,y)
    rect = RectComponent(self, 20,20)
    playerPositionComponent = PlayerPositionComponent(self, animalType)

    


    if animalType == AnimalType.BABY_DRAGON:
      #"Animals/babyDragon.png"
      rect.setColour(Color(255,0,255))
    elif animalType == AnimalType.BAT:
      #"Animals/bat.png"
      rect.setColour(Color(0,0,255))
    elif animalType == AnimalType.SALAMANDER:
      #"Animals/salamander.png"
      rect.setColour(Color(0,255,0))
    elif animalType == AnimalType.SPIDER:
      #"Animals/spider.png"
      rect.setColour(Color(255,0,0))


    # spriteComponent = SpriteComponent(self, 20, 20,path)
    
    self.add_component(trans)
    self.add_component(rect)
    self.add_component(playerPositionComponent)
    # self.add_component(spriteComponent)