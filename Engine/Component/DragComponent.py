from Engine import Entity
from .Component import Component


from Engine.Component.ClickableComponent import ClickableComponent
from Engine.Component.TransformComponent import TransformComponent
from Engine.Input import Input

class DragComponent(Component):
  def __init__(self, owner: Entity):
    self.owner = owner

    self.x_offset = 0
    self.y_offset = 0

    self.grabbed = False
    
  def update(self):
    # do different things based on click state
    ck: ClickableComponent = self.owner.get_component(ClickableComponent)
    tc: TransformComponent = self.owner.get_component(TransformComponent)

    if ck == None or tc == None:
      return 

    # todo another implementation would be listenting to this to be clicked??
    # todo maybe this game would have way better performance if it was just a bunch of mouse
    # todo click listeners 
    if self.grabbed == False:
      if ck.clicked:
        self.grabbed = True
        self.x_offset = tc.x - Input.getmouseposition()[0]
        self.y_offset = tc.y - Input.getmouseposition()[1]
    else:
      if ck.clicked:
        # match transform to mouse position 
        tc: TransformComponent = self.owner.get_component(TransformComponent)
        tc.x = Input.getmouseposition()[0] + self.x_offset
        tc.y = Input.getmouseposition()[1] + self.y_offset

        #todo can drop off screen, use screen manager to manage this 

        
      else:
        self.grabbed = False
  
        
 


    