from engine.command.Command import Command
from fieryDragons.Player import Player
from fieryDragons.enums.AnimalType import AnimalType
import pdb  

class SwapPlayerCommand(Command):
    # pdb.set_trace()  
    def run(self):
        active_player = Player.ACTIVE_PLAYER
        players = active_player.traverse(active_player, True)
        
        # Finding the closest player
        min_distance = float('inf')
        closest_player = None
        for player in players:
            if not player.getPosition().isCave():
                # modify player position
                distance = abs(active_player.position - player.position)
                if distance < min_distance:
                    min_distance = distance
                    closest_player = player
                    
        
        # Swap positions if a closest player is found
        if closest_player:
            # transfom 
            temp_transform = active_player.transformComponent.clone()
            closest_player_copy = closest_player.transformComponent.clone()

            active_player.transformComponent.copy(closest_player_copy)

            closest_player.transformComponent.copy(temp_transform)
            

        

        active_player.endTurn()
