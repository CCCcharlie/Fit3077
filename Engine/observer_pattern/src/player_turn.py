# player_turn.py

from emitter import Emitter

class PlayerTurn(Emitter):
    def end_turn(self, player):
        message = f"Player {player}'s turn has ended."
        self.notify(message)
