from abc import abstractmethod

from engine.scene.Scene import Scene


class SceneBuilder:
  @abstractmethod
  def build(self) -> Scene:
    raise NotImplementedError()