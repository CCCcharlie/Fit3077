from engine.builder.SceneBuilder import SceneBuilder
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.CircularSegmentTrapezoidComponent import CircularSegmentTrapezoidComponent
from engine.entity.Entity import Entity
from engine.utils.Vec2 import Vec2
from pygame import Color
from ..entity.ChitCardBuilder import ChitCardBuilder
from engine.scene.Scene import Scene


class TestCircularSegmentTrapBuilder(SceneBuilder):
  def __init__(self):
    return

  def build(self) -> Scene:
    s = Scene()

    e = Entity()
    
    transform = TransformComponent()
    transform.position = Vec2(750,500)
    transform.rotate(180)
    render = CircularSegmentTrapezoidComponent(
      transform, 
      30, 
      200, 
      180, 
      Color(0,0,0))


    e.add_renderable(render)

    s.addEntity(e)

    return s
