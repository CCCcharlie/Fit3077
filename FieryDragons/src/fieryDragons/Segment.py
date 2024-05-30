from engine.component.TransformComponent import TransformComponent
from engine.utils.Vec2 import Vec2
from fieryDragons.enums.AnimalType import AnimalType


class Segment():
  def __init__(self, transformComponent: TransformComponent, animalType: AnimalType, offset: Vec2 = Vec2(0,0)):
    self.__animalType: AnimalType = animalType

    self.__snapTransform = transformComponent.clone()
    self.__snapTransform.position += offset

  def getAnimalType(self) -> AnimalType:
    return self.__animalType
  
  def getSnapTransform(self) -> TransformComponent:
    return self.__snapTransform.clone()


