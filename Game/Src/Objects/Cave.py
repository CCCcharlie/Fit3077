from Engine import *

from Game.Src.Components.PlayerPositionComponent import PlayerPositionComponent
from Game.Src.Enums.AnimalType import AnimalType

class Cave(Entity):
  def __init__(self, x, y, animalType: AnimalType):
    super().__init__()

    path = ""
    colour = (0,0,0)
    if animalType == AnimalType.BABY_DRAGON:
      path = "Animals/babyDragon.png"
      colour = (255,0,255)
    elif animalType == AnimalType.BAT:
      path = "Animals/bat.png"
      colour = (0,0,255)
    elif animalType == AnimalType.SALAMANDER:
      path = "Animals/salamander.png"
      colour = (0,255,0)
    elif animalType == AnimalType.SPIDER:
     path = "Animals/spider.png"
     colour = (255,0,0)

    trans = TransformComponent(self,x,y)
    rect = RectComponent(self, 20,20,colour)
    playerPositionComponent = PlayerPositionComponent(self, animalType)


    # spriteComponent = SpriteComponent(self, 20, 20,path)
    
    self.add_component(trans)
    self.add_component(rect)
    self.add_component(playerPositionComponent)
    # self.add_component(spriteComponent)