import Component 

class SpriteComponent(Component):
  def __init__(self, owner, image=None):
    super().__init__(owner)

    if (image==None):
      # todo load in pink square ... 
      pass
    self.image = image