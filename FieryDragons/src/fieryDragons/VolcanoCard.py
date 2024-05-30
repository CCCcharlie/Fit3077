from __future__ import annotations

from typing import List

from engine.component.TransformComponent import TransformComponent
from engine.utils.Vec2 import Vec2
from fieryDragons.Segment import Segment
from fieryDragons.enums.AnimalType import AnimalType


class VolcanoCard():
  def __init__(self, segments: List[Segment], cave: Segment | None):
    self.__segments: List[Segment] = segments
    self.__cave: Segment = cave

    self.__next: VolcanoCard = None
  
  def setNext(self, segment: VolcanoCard):
    self.__next = segment

  def generatePath(self) -> List[Segment]:
    # INITIAL CASE add cave and segments that come after the cave 
    # add cave to start of path
    path: List[Segment] = [self.__cave]

    # add segments that come after the cave 
    numSegmentsBeforeCave: int = len(self.__segments) // 2

    for i in range(numSegmentsBeforeCave, len(self.__segments)):
      path.append(self.__segments[i]) 

    restOfPath = self._generatePath(self.__cave)
    path.extend(restOfPath)
    return path

  def _generatePath(self, startCave: Segment) -> List[Segment]:
    # BASE CASE this volcano card has the cave 
    if startCave == self.__cave:
      result = []
      numSegmentsBeforeCave: int = len(self.__segments) // 2
      for i in range(0, numSegmentsBeforeCave):
        result.append(self.__segments[i])
      result.append(self.__cave)
      return result

    # RECURSIVE STEP 
    # add this caves segments and continue recursion
    result = self.__segments.copy()
    restOfList = self.__next._generatePath(startCave)
    result.extend(restOfList)

    return result
  


