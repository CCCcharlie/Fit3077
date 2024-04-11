from Engine import Entity
from .Component import Component
from Engine.Component.TransformComponent import TransformComponent
from Engine.Command.Command import Command
from Engine.Component.CommandComponent import CommandComponent
import pygame
import math

#todo add parameters to this component 
class AnimatedComponent(Component):
  def __init__(self, owner: Entity):
    super().__init__(owner)

    self.sprites = ['L1.png', 'L2.png', 'L3.png', 'L4.png', 'L5.png', 'L6.png', 'L7.png', 'L8.png', 'L9.png']

    self.animationSpeed = 0.2

    # load all sprites 
    self.image_surfaces = []
    for sprite in self.sprites:
      image_surface = pygame.image.load("Game/Assets/Walk/" + sprite).convert_alpha()
      self.image_surfaces.append(image_surface)

    self.image_index = 0
    self.animationFinishTrigger: Command = None
   

  def update(self):
    self.image_index += 1 * self.animationSpeed

    if self.image_index >= len(self.sprites):
      if self.animationFinishTrigger != None:
        cc: CommandComponent = self.owner.get_component(CommandComponent)
        if cc != None:
          cc.owner.add_component(self.animationFinishTrigger)

    # todo also add options for one play through etc ... 
    self.image_index = self.image_index % len(self.sprites)

  def render(self, display_surf):
    tc: TransformComponent = self.owner.get_component(TransformComponent)

    if tc != None:
      #Add sprite to display coords
      display_surf.blit(self.image_surfaces[math.floor(self.image_index)], (tc.x, tc.y))



