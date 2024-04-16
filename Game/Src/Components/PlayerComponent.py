from Engine import *
from Game.Src.Enums.AnimalType import AnimalType 

class PlayerComponent(Component):
  def __init__(self, owner: Entity, startingAnimal: AnimalType):
    super().__init__(owner)
    self.startingAnimal: AnimalType = startingAnimal

