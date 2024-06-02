from typing import List
from engine.command.Command import Command
from engine.command.LinearMoveMFCommand import LinearMoveMFCommand
from engine.component.TransformComponent import TransformComponent
from fieryDragons.Player import Player
from fieryDragons.Segment import Segment



class SwapCommand(Command):
    """
    Shuffle the ChitCards by rearranging the order
    """
    def __init__(self):
        pass

    def run(self):
        # first get the active player
        player: Player = Player.ACTIVE_PLAYER

        other_players: List[Player] = player.traverse(player, True)

        playerPositions: List[Segment] = [player.getPosition() for player in other_players]

        #temp (get the distance for each player to each segment)
        closestPlayer: Player | None = other_players[0]

        # player looses their turn 


        # if no player is found then this chit card is done 
        if closestPlayer is None:
            return 
        
        #get the segments of each player
        closestPlayerSegment: Segment = closestPlayer.getPosition()
        swapPlayerSegment: Segment = player.getPosition()

        # move players
        player.moveToSegment(closestPlayerSegment)
        closestPlayer.moveToSegment(swapPlayerSegment)

        # update path ... position


        
