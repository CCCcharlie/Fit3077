from Engine import *
from Game.Src.Objects.Segment import Segment
from Game.Src.Objects.Cave import Cave

from typing import List

class VolcanoCard(Entity):
  def __init__(self, segments: List[Segment], cave: Cave=None):
    super().__init__()

    trans = TransformComponent(self,20,20)
    self.add_component(trans)
    

    ## add children
    for segment in segments:
      child_comp = ChildComponent(self, segment)
      self.add_component(child_comp)    

    # add cave if have
    if cave != None:
      self.add_component(cave)

