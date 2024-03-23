
import pygame
from Engine import Entity
from Engine.Component import ClickableComponent, RectComponent, TextComponent, TransformComponent, DragComponent

# https://refactoring.guru/design-patterns/builder
# maybe im not too sure how we want to do this 


# TODO this should just have a collider, a transform to modify, no text, rect, or clickable
class Dragable(Entity):
  def __init__(self, x, y, width, height, textContent):
    super().__init__()

    trans = TransformComponent(self, x, y)
    rect = RectComponent(self, width, height, (0,0,250))
    text = TextComponent(self, textContent, pygame.font.SysFont("Corbel", 30), (250,250,250))
    clickable = ClickableComponent(self, width, height)
    drag = DragComponent(self)

    self.add_component(trans)
    self.add_component(rect)
    self.add_component(text)
    self.add_component(clickable)
    self.add_component(drag)
