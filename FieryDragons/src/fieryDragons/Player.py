

from typing import List
from engine.component.TransformComponent import TransformComponent
from fieryDragons.Segment import Segment
from fieryDragons.TurnManager import TurnManager
from fieryDragons.enums.AnimalType import AnimalType


class Player:
  def __init__(self, startingSegment: Segment, transformComponent: TransformComponent):
    self.position: int = 0
    self.path: List[Segment] = startingSegment.generatePath(startingSegment)
    self.transformComponent = transformComponent
    
  def getPosition(self) -> Segment:
    return self.path[self.position]

  def move(self, animalType: AnimalType, amount: int):

    if animalType is AnimalType.PIRATE_DRAGON:
      newLocation = self.position - amount
      newSegment = self.path[newLocation]

      if TurnManager().canMove(self, newSegment):
        self.position = newLocation
        self.transformComponent.position = newSegment.getSnapPosition()
        self.transformComponent.rotation = newSegment.getSnapRotation()

      # end turn 
      TurnManager().nextTurn()

  
    if animalType is self.path[self.position].getAnimalType():
      newLocation = self.position + amount
      newSegment = self.path[newLocation]

      #check can move there 
      if TurnManager().canMove(self, newSegment):
        self.position = newLocation
        self.transformComponent.position = newSegment.getSnapPosition()
        self.transformComponent.rotation = newSegment.getSnapRotation()
      else:
        TurnManager().nextTurn()


    #end turn
    TurnManager().nextTurn()



    

    
    
  

