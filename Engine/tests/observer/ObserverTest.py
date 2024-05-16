# test.py

from player_turn import PlayerTurn
from chit_card import ChitCard

# Create instances
player_turn = PlayerTurn()
chit_card = ChitCard()

# Subscribe chit_card to player_turn
player_turn.subscribe(chit_card)

# Simulate player's turn ending
player_turn.end_turn("Player 1")
