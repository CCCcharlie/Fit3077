import pygame

class ChitCard:
    colors = {
        'Salamander': (255, 0, 0),     # Red
        'Bat': (128, 0, 128),          # Purple
        'Spider': (64, 64, 64),           # Black
        'Baby Dragon': (0, 255, 0),    # Green
        'Pirate Dragon': (128, 128, 128) # White
    }

    # Positions in a 4x4 grid within a 250x250 space
    positions = [
        (200, 200), (270, 200), (340, 200), (410, 200),
        (200, 270), (270, 270), (340, 270), (410, 270),
        (200, 340), (270, 340), (340, 340), (410, 340),
        (200, 410), (270, 410), (340, 410), (410, 410)
    ]

    def __init__(self, animal_type, count, index):
        self.animal_type = animal_type
        self.count = count
        self.index = index
        self.position = ChitCard.positions[index]

    def draw(self, surface):
        pygame.draw.rect(surface, ChitCard.colors[self.animal_type],
                         (self.position[0], self.position[1], 20, 20))

    def update_position(self, new_index):
        self.index = new_index
        self.position = ChitCard.positions[new_index]

    def __repr__(self):
        return f"{self.count} x {self.animal_type} at {self.position}"