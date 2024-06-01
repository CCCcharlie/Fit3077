from engine.component.TransformComponent import TransformComponent
from engine.utils.Vec2 import Vec2
from fieryDragons.enums.AnimalType import AnimalType


class Segment():
  def __init__(self, snapTransform: TransformComponent, animalType: AnimalType):
    self.__animalType: AnimalType = animalType
    self.__snapTransform: TransformComponent = snapTransform.clone()

  def getAnimalType(self) -> AnimalType:
    return self.__animalType
  
  def getSnapTransform(self) -> TransformComponent:
    return self.__snapTransform.clone()


