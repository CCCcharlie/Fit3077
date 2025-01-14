from dataclasses import dataclass
from typing import Tuple
import math

@dataclass
class Vec2:
  x: float
  y: float

  def toTuple(self) -> Tuple[float, float]:
    return (self.x, self.y)
  
  def __add__(self, other):
    return Vec2(self.x + other.x, self.y + other.y)
    
  def __sub__(self, other):
    return Vec2(self.x - other.x, self.y - other.y)
  
  def __mul__(self, scalar):
    return Vec2(self.x * scalar, self.y * scalar)
  
  def __neg__(self):
    return Vec2(-self.x, -self.y)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def distance(self, other: 'Vec2') -> float:
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
  
  def clone(self):
    return Vec2(self.x, self.y)
  
  
