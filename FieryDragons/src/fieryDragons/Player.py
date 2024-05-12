

from fieryDragons.Segment import Segment
from fieryDragons.enums.AnimalType import AnimalType


class Player:
  def __init__(self, startingSegment: Segment):
    self.position = 0
    self.path = startingSegment.generatePath(startingSegment)

  def move(self, animalType: AnimalType, amount: int):
    if animalType is AnimalType.PIRATE_DRAGON:
      newLocation = self.position - amount
      # move there
      # end turn

  
    if animalType is self.path[self.position].getAnimalType():
      newLocation = self.position + amount
      # move there

    #end turn



    

    
    
  

