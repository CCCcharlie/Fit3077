from typing import List

from engine.component.TransformComponent import TransformComponent
from engine.utils.Vec2 import Vec2
from fieryDragons.enums.AnimalType import AnimalType


class Segment():
  def __init__(self, transformComponent: TransformComponent, animalType: AnimalType, offset: Vec2 = Vec2(0,0)):
    self.__offset: Vec2 = offset
    self.__transformComponent: TransformComponent = transformComponent
    self.__animalType: AnimalType = animalType

    self.__next: 'Segment' = None
    self.__cave: 'Segment' = None

  def setNext(self, segment: 'Segment'):
    self.__next = segment

  def setCave(self, cave: 'Segment'):
    self.__cave = cave

  def getNext(self) -> 'Segment':
    return self.__next
  
  def getCave(self) -> 'Segment':
    return self.__cave

  def getAnimalType(self) -> AnimalType:
    return self.__animalType
  
  def getSnapPosition(self) -> Vec2:
    #TODO rotate the offset based on the transform's rotation
    return self.__transformComponent.position + self.__offset
  
  def getSnapRotation(self) -> Vec2:
    return self.__transformComponent.rotation
  
  def generatePath(self, start: 'Segment') -> List['Segment']:
    segmentList: List[Segment] = []
    segmentList.append(start) # add cave
    segmentList.append(start.getNext()) # add first stop
    segmentList.append(start.getNext().getNext()) # add second stop 

    searching: bool = True
    currentSpot: 'Segment' = start.getNext().getNext()

    while searching:
      if currentSpot.getCave() == start:
        searching = False
        segmentList.append(currentSpot.getCave())
      else:
        segmentList.append(currentSpot.getNext())
        currentSpot = currentSpot.getNext()
    return segmentList


