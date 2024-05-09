from main.engine.utils.Vec2 import Vec2

class TransformComponent():
  def __init__(self):
    self._position: Vec2 = Vec2(0,0) 
    self._scale: Vec2 = Vec2(1,1)
    self._rotation: int = 0

  @property
  def position(self) -> Vec2:
    return self._position

  @position.setter
  def position(self, value: Vec2) -> None:
    self._position = value

  @property
  def scale(self) -> Vec2:
    return self._scale

  @scale.setter
  def scale(self, value: Vec2) -> None:
    self._scale = value

  @property
  def rotation(self) -> int:
    return self._rotation

  @rotation.setter
  def rotation(self, value: int) -> None:
    self._rotation = value % 365

  def rotate(self, angle: int) -> None:
    self._rotation += angle
    self._rotation = self.rotation % 365