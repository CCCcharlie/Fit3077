from Engine import *
from Game.Src.Enums.AnimalType import AnimalType
from Game.Src.Objects.TurnManager import TurnManager


class PlayerPositionComponent(Component):
  def __init__(self, owner: Entity, animal: AnimalType):
    self.owner = owner
    self.animal = animal
    self.playerOnSquare: Entity = None

    self.next: PlayerPositionComponent = None
    self.previous: PlayerPositionComponent = None
    self.cave: PlayerPositionComponent = None

  def movePlayer(self, player: Entity, moveDistance):
    #try to move forward
    if moveDistance > 0:
      if self.next.movePlayer(player, moveDistance - 1):
        return True # could move forward

    #try to move back
    if moveDistance < 0:
      if(self.previous.movePlayer(player, moveDistance + 1)):
        return True # could move back
      

    #move it here 
    if self.addPlayer(player):
      return True # could move it here

    # who called this must take it 
    return False

    
  def addPlayer(self, player: Entity):
    #if player is already here then we cant move here
    if self.playerOnSquare != None:
      return False     

    tc_player: TransformComponent = player.get_component(TransformComponent)
    if tc_player is None:
      print("Player needs a transform component in player position component.addPlayer")
      return False
    
    tc: TransformComponent = self.owner.get_component(TransformComponent)
    if tc is None:
      print("Player position component needs a transform component")
      return False
    
    tc_player.x = tc.x
    tc_player.y = tc.y

    self.playerOnSquare = player

    TurnManager.CURRENT_POSITION = self
    


