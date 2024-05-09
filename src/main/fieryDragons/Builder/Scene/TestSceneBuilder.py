from src.main.engine import Scene, Entity, RectComponent, TransformComponent, Vec2
import pygame

class TestSceneBuilder:
  def __init__(self):
    return
  
  def build(self) -> Scene:
    scene = Scene()

    e = Entity()
    tc = TransformComponent()
    tc.position = Vec2(10,10)
    e.add_renderable(RectComponent(tc, 40, 40, pygame.Color(255,255,255)))
    
    scene.addEntity(e)

    return scene