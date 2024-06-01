from __future__ import annotations
from typing import Dict

from engine.Serializable import Serializable


from ..utils.Vec2 import Vec2


class TransformComponent(Serializable):
  def __init__(self):
    self._position: Vec2 = Vec2(0,0) 
    self._scale: Vec2 = Vec2(1,1)
    self._rotation: int = 0

  @property
  def position(self) -> Vec2:
    return Vec2(self._position.x, self._position.y)

  @position.setter
  def position(self, value: Vec2) -> None:
    self._position = Vec2(value.x, value.y)

  @property
  def scale(self) -> Vec2:
    return Vec2(self._scale.x, self._scale.y)

  @scale.setter
  def scale(self, value: Vec2) -> None:
    self._scale = Vec2(value.x, value.y)

  @property
  def rotation(self) -> int:
    return self._rotation

  @rotation.setter
  def rotation(self, value: int) -> None:
    self._rotation = value % 365

  def rotate(self, angle: int) -> None:
    self._rotation += angle
    self._rotation = self.rotation % 360

  def clone(self) -> TransformComponent:
    t = TransformComponent()
    t.position = self.position
    t.rotation = self.rotation
    t.scale = self.scale
    return t
  
  def copy(self, t: TransformComponent):
    """
    Copy the position, rotation and scale of the other transform
    """
    self._position = t.position.clone()
    self._rotation = t.rotation
    self._scale = t.scale.clone()

  def serialise(self) -> Dict:
    d: Dict = {}

    d["position"] = {
      "x": self.position.x,
      "y": self.position.y
    }
    d["rotation"] = self.rotation
    d["scale"] = {
      "x": self.scale.x,
      "y": self.scale.y
    }

    return d
  
  def deserialise(self, data: Dict) -> None:
    position = data["position"]
    rotation = data["rotation"]
    scale = data["scale"]

    positionVec = Vec2(float(position["x"]), float(position['y']))
    rotationInt = int(rotation)
    scaleVec = Vec2(float(scale['x']), float(scale['y']))

    self.position = positionVec
    self.rotation = rotationInt
    self.scale = scaleVec
    return None
