from typing import List
from engine.command.Command import Command
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.component.TransformComponent import TransformComponent
from fieryDragons.Player import Player
from fieryDragons.Segment import Segment
from fieryDragons.observer.PlayerTurnEndEmitter import PlayerTurnEndEmitter



class SwapCommand(Command):
    """
    Shuffle the ChitCards by rearranging the order
    """
    def __init__(self):
        pass

    def run(self):
        
        # first get the active player
        player: Player = Player.ACTIVE_PLAYER

        # player looses their turn 
         #end the active players turn
        if Player.ACTIVE_PLAYER is not None:
            Player.ACTIVE_PLAYER.endTurn()
        PlayerTurnEndEmitter().notify()

        # get all player distances 
        other_players: List[Player] = player.traverse(player, True)
        distances = [player.getDistanceToPlayer(other_player) for other_player in other_players]

        # if no players can be found 
        non_none_distances = [(i, d) for i, d in enumerate(distances) if d is not None]
        if not non_none_distances:
            return
        
        # Find the closest player
        smallest_index, smallest_value = min(non_none_distances, key=lambda x: x[1])
        closestPlayer: Player = other_players[smallest_index]

        #get the segments of each player
        closestPlayerSegment: Segment = closestPlayer.getPosition()
        swapPlayerSegment: Segment = player.getPosition()

        # move players
        player.forceMoveToSegment(closestPlayerSegment)
        closestPlayer.forceMoveToSegment(swapPlayerSegment)



        
