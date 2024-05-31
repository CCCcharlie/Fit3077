from engine.command.Command import Command
from fieryDragons.Player import Player
from fieryDragons.enums.AnimalType import AnimalType

class SwapPlayerCommand(Command):
    def run(self):
        active_player = Player.ACTIVE_PLAYER
        players = active_player.traverse(active_player, True)
        
        # Finding the closest player
        min_distance = float('inf')
        closest_player = None
        for player in players:
            if not player.getPosition().isCave():
                distance = abs(active_player.position - player.position)
                if distance < min_distance:
                    min_distance = distance
                    closest_player = player
        
        # Swap positions if a closest player is found
        if closest_player:
            temp_position = active_player.position
            temp_transform = active_player.transformComponent.clone()

            active_player.position = closest_player.position
            active_player.transformComponent.copy(closest_player.transformComponent)

            closest_player.position = temp_position
            closest_player.transformComponent.copy(temp_transform)
            
            # Move to the new position
            active_player._moveToSegment(active_player.getPosition())
            closest_player._moveToSegment(closest_player.getPosition())

        active_player.endTurn()
