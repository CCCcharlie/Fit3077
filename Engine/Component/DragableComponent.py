from Engine import Entity
from .Component import Component

from enum import Enum 
from Engine.Component.ClickableComponent import ClickableComponent
from Engine.Component.TransformComponent import TransformComponent
from Engine.Component.RectComponent import RectComponent
from Engine.Input import Input


#todo remove the colour stuff and just do dragging 
class DragableComponent(Component):
  def __init__(self, owner: Entity):
    self.owner = owner

    self.x_offset = 0
    self.y_offset = 0
    
    # python doesnt have a switch statemnet so we just switched dictionary method 
    self.switcher = {
      1: self.normal_update,
      2: self.hovered_update,
      3: self.held_update,
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
        # transform to held state but get x,y offset from transform position
        # get transform componet 
        tc: TransformComponent = self.owner.get_component(TransformComponent)
        if tc != None:
          self.x_offset = tc.x - Input.getmouseposition()[0]
          self.y_offset = tc.y - Input.getmouseposition()[1]
        return 3  # hover and clicked -> held
      return 2    # hover -> hover 
    return 1      #  -> normal 

  def held_update(self, ck: ClickableComponent):
    # check if still hovering 
    if ck.hover:
      if ck.clicked:
        # match transform to mouse position 
        tc: TransformComponent = self.owner.get_component(TransformComponent)
        tc.x = Input.getmouseposition()[0] + self.x_offset
        tc.y = Input.getmouseposition()[1] + self.y_offset
        return 3
      # just dropped
      self.x_offset = 0
      self.y_offset = 0
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

    