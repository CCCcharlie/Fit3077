import pygame

class VolcanoCard:
    card_width = 90
    card_height = 30

    colors = {
        'Baby Dragon': (0, 255, 0),    # Green
        'Salamander': (255, 0, 0),     # Red
        'Bat': (128, 0, 128),          # Purple
        'Spider': (64, 64, 64)            # Black
    }

    card_orders = [
        ['Baby Dragon', 'Bat', 'Spider'],
        ['Salamander', 'Spider', 'Bat'],
        ['Spider', 'Salamander', 'Baby Dragon'],
        ['Bat', 'Spider', 'Baby Dragon'],
        ['Spider', 'Bat', 'Salamander'],
        ['Baby Dragon', 'Salamander', 'Bat'],
        ['Bat', 'Baby Dragon', 'Salamander'],
        ['Salamander', 'Baby Dragon', 'Spider']
    ]

    #index signfiys which hard coded card it is
    def __init__(self, index, has_cave=False):
        self.animals = VolcanoCard.card_orders[index]
        self.position = (0, 0)  # Default position
        self.has_cave = has_cave  # Indicates if the card has an indentation for a cave

    def draw(self, surface):
        x, y = self.position
        for i, animal in enumerate(self.animals):
            segment_width = VolcanoCard.card_width // len(self.animals)
            pygame.draw.rect(surface, VolcanoCard.colors[animal],
                             (x + i * segment_width, y, segment_width, VolcanoCard.card_height))
