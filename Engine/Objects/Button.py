
import pygame
from Engine import Entity
from Engine.Command import Command
from Engine.Component import ClickableComponent, CommandComponent, RectComponent, TextComponent, TransformComponent, ButtonComponent
from Engine.Component.HitboxComponent.RectHitboxComponent import RectHitboxComponent

# https://refactoring.guru/design-patterns/builder
# maybe im not too sure how we want to do this 
class Button(Entity):
  def __init__(self, x, y, width, height, textContent, command: Command):

    super().__init__()

    trans = TransformComponent(self, x, y)
    rect = RectComponent(self, width, height, (0,0,250))
    text = TextComponent(self, textContent, pygame.font.SysFont("Corbel", 30), (250,250,250))
    clickable = ClickableComponent(self, width, height)
    button = ButtonComponent(self, command)
    command = CommandComponent(self)
    hitbox = RectHitboxComponent(self, width, height)

    self.add_component(trans)
    self.add_component(rect)
    self.add_component(text)
    self.add_component(clickable)
    self.add_component(button)
    self.add_component(command)
    self.add_component(hitbox)


