
from Engine import Entity
from Engine.Component.HitboxComponent.HitboxComponent import HitboxComponent
from .Component import Component
from Engine.Input import Input
from Engine.Component.TransformComponent import TransformComponent


class ClickableComponent(Component):
  def __init__(self, owner: Entity, width: int, height: int):
    super().__init__(owner)
    self.width = width
    self.height = height


    self.hover = False
    self.clicked = False

  def update(self):
    # get owner transform coords 
    tc: TransformComponent = self.owner.get_component(TransformComponent)
    if tc is None:
      print("Clickable needs a Trasnform Component")
      return

    # x range is tc.x -> tc.x + self.width
    # y range is tx.y -> tc.y + self.height
    mx, my = Input.getmouseposition()


    hitbox: HitboxComponent = self.owner.get_component(HitboxComponent)
    if hitbox is None:
      print("Clickable needs a Hitbox Component")
      return
    
    self.hover = hitbox.checkPointCollision(mx,my)

    if self.hover is None:
      print("Clickable needs valid hitbox check")
      return

    if (self.hover):
      self.clicked = Input.getMouseButton(1)
    else:
      # clicked may still be true as lagging behind 
      # however we still need to drop it if they deselect
      if self.clicked:
        self.clicked = Input.getMouseButton(1)
     


  # interface part 
  def get_hover(self):
    return self.hover
  
  def get_clicked(self):
    return self.clicked 


