from src.main.engine.Entity import Entity
from src.main.engine.utils.Vec2 import Vec2
from src.main.fieryDragons.builder.entity.ChitCardBuilder import ChitCardBuilder
from src.main.engine.Scene import Scene


class TestChitCardSceneBuilder:
  def __init__(self):
    return

  def build(self) -> Scene:
    s = Scene()

    chitCardBuilder = ChitCardBuilder(20)

    for i in range(4):
      for j in range(4):
        chitCardBuilder.setPosition(Vec2(10 + i * 40, 10 + j * 40)) 
        cc: Entity = chitCardBuilder.build()

        s.addEntity(cc)

    return s
