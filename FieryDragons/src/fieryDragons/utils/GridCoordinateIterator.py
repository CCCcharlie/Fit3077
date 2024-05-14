from typing import Iterator

from engine.utils.Vec2 import Vec2


class GridCoordinateIterator(Iterator[Vec2]):
  def __init__(
      self, rows: int, columns: int, center: Vec2, width: int, height: int
  ):
    self.__rows = rows
    self.__columns = columns
    self.__center = center
    self.__width = width
    self.__height = height
    self.__n = 0

    self.__nElements = self.__rows * self.__columns
  

  def __inter__(self)-> Iterator[Vec2]:
    return self
  

  def __next__(self) -> Vec2:
    # end after all ements placed
    if self.__n >= self.__nElements:
      raise StopIteration()

    # Calculate row and column
    row = self.__n // self.__columns
    column = self.__n % self.__columns

    #Calculate coords based on current row and column
    x = self.__center.x - (self.__width // 2) + (column * self.__width // self.__columns)
    y = self.__center.y - (self.__height // 2) + (row * self.__height // self.__rows)

    self.__n += 1 

    return Vec2(x, y)
