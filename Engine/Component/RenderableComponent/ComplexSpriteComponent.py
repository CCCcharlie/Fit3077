from typing import List
from pygame import Surface
from Engine import Entity
from Engine.Component.RenderableComponent.RenderableComponent import RenderableComponent

class ComplexSpriteComponent(RenderableComponent):
  def __init__(self, owner: Entity, sprites: List[RenderableComponent]):
    self.sprites = sprites
    super().__init__(owner)


  def render(self, display_surf: Surface):
    if self.showing is False:
      return 
  
    # render each sub 
    for sprite in self.sprites:
      sprite.render(display_surf)


