from engine.command.Command import Command
from fieryDragons.Player import Player
class SwapPlayerCommand(Command):
    def run(self):
        active_player = Player.ACTIVE_PLAYER
        players = active_player.traverse(active_player, True)
        
        # finding closest path 
        min_distance = float('inf')
        closest_player = None
        for player in players:
            if not player.getPosition().isCave():
                distance = abs(active_player.position - player.position)
                if distance < min_distance:
                    min_distance = distance
                    closest_player = player
        
        # swap
        if closest_player:
            active_player_position = active_player.position
            active_player.position = closest_player.position
            closest_player.position = active_player_position
            
            # move to the new position
            active_player._moveToSegment(active_player.getPosition())
            closest_player._moveToSegment(closest_player.getPosition())

        active_player.endTurn()
