import pygame 
from pygame.locals import *
from typing import List

from Engine import Entity
from Engine.Component.TransformComponent import TransformComponent
from Engine.Component import Component
from Engine.Command import Command

class CommandComponent(Component):
  def __init__(self, owner: Entity):
    super().__init__(owner)

    self.commands: List[Command] = []


  def update(self):
    # process all pending commands
    for command in self.commands:
      command.run()
    
    self.commands.clear()

  def addCommand(self, command: Command):
    self.commands.append(command)
    
    

