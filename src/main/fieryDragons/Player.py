from main.fieryDragons.Segment import Segment


class Player:
  def __init__(self, startingSegment: Segment):
    self.position = 0
    self.path = startingSegment.generatePath(startingSegment)
  

