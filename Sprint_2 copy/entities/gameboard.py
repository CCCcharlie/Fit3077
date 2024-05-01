import random
from .volcanocard import VolcanoCard

class GameBoard:
    def __init__(self, num_cards):
        # Create VolcanoCard instances with random cave assignments
        self.cards = [VolcanoCard(i % len(VolcanoCard.card_orders), has_cave=random.choice([True, False]))
                      for i in range(num_cards)]
        # Define the positions within the gameboard class
        self.positions = [
            (100, 100), (300, 100), (500, 100),
            (100, 300), (500, 300),
            (100, 500), (300, 500), (500, 500)
        ]
        # Initially assign positions to cards
        self.assign_positions()

    def shuffle_volcano_cards(self):
        # Shuffle the positions
        random.shuffle(self.positions)
        # Reassign the shuffled positions to the cards
        self.assign_positions()

    def assign_positions(self):
        # Assign each card a position from the shuffled list
        for card, position in zip(self.cards, self.positions):
            card.position = position