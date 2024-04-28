from Engine import Entity

from .Component import Component

from enum import Enum 
from Engine.Component.ClickableComponent import ClickableComponent
from Engine.Component.RenderableComponent.RectComponent import RectComponent
from Engine.Component.CommandComponent import CommandComponent
from Engine.Command.Command import Command

class ButtonComponent(Component):
  def __init__(self, owner: Entity, command: Command):
    self.owner = owner
    self.command = command
    
    # python doesnt have a switch statemnet so we just switched dictionary method 
    self.switcher = {
      1: self.normal_update,
      2: self.hovered_update,
      3: self.pressed_update,
    }

    self.colour_switcher = {
      1: "#003049",
      2: "#669bbc",
      3: "#c1121f",
    }
    self.state = 1

  def normal_update(self, ck: ClickableComponent):
    # check if hover 
    if ck.hover:
      return 2
    return 1

  def hovered_update(self, ck: ClickableComponent):
    if ck.hover:
      if ck.clicked:
        return 3  # hover and clicked -> pressed
      return 2    # hover -> hover 
    return 1      #  -> normal 

  def pressed_update(self, ck: ClickableComponent):
    # check if still hovering 
    if ck.hover:
      if ck.clicked:
        return 3
      # add command to command component
      cc: CommandComponent = self.owner.get_component(CommandComponent)
      if cc != None:
        cc.addCommand(self.command)
      return 2
    return 1

  def default(self, ck: ClickableComponent):
    print("Button was in default mode :(")
    return 1

  def update(self):
    # do different things based on click state
    ck: ClickableComponent = self.owner.get_component(ClickableComponent)

    if ck != None:
      self.state = self.switcher.get(self.state, self.default)(ck) 
      
      # get colour from state 
      colour = self.colour_switcher.get(self.state, self.default)

      # update renderer 
      # ideally we want render component not rect ....
      rc: RectComponent = self.owner.get_component(RectComponent)
      if rc != None:
        rc.setColour(colour)

    