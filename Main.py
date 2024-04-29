import pygame
import random
import math

# Define constants for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define constants for screen dimensions and other parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Define class for Chit Card
class ChitCard:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        # Draw chit card
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)

# Define class for Volcano Card
class VolcanoCard:
    def __init__(self, x, y, width, height, segments):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.segments = segments

    def draw(self, screen):
        # Draw dividing lines
        num_divisions = len(self.segments)
        division_width = self.width / num_divisions
        for i in range(1, num_divisions):
            pygame.draw.line(screen, BLACK, (self.x + i * division_width, self.y),
                            (self.x + i * division_width, self.y + self.height), 2)

        # Draw volcano card segments
        for i, has_cave in enumerate(self.segments):
            if has_cave:
                color = BLACK  # Segment with cave
            else:
                color = WHITE  # Empty segment
            segment_x = self.x + i * division_width
            segment_y = self.y
            segment_width = division_width
            segment_height = self.height
            # Draw segment rectangle with black outline
            pygame.draw.rect(screen, BLACK, (segment_x, segment_y, segment_width, segment_height), 2)
            if has_cave:
                # Draw segment rectangle with filled color if there is a cave
                pygame.draw.rect(screen, color, (segment_x + 2, segment_y + 2, segment_width - 4, segment_height - 4))

# Define class for GameBoard
class GameBoard:
    def __init__(self):
        self.volcano_cards = []
        self.chit_cards = []
        self.num_volcano_cards = 8  # Number of volcano cards
        self.num_caves = 4  # Number of cave segments per volcano card

    def initialize_board(self):
        # Create chit cards in the center
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        num_chit_cards = 16
        chit_card_width = 40
        chit_card_height = 60
        chit_card_spacing = 10
        chit_cards = []
        for i in range(num_chit_cards):
            x = center_x - chit_card_width // 2 + (i % 4) * (chit_card_width + chit_card_spacing)
            y = center_y - chit_card_height // 2 + (i // 4) * (chit_card_height + chit_card_spacing)
            chit_cards.append((x, y))

        # Calculate the center of the ring
        ring_center_x = center_x
        ring_center_y = center_y

        # Calculate the radius of the ring based on the distance between the center of the ring and the chit cards
        radius = 200

        # Calculate the angle increment for each volcano card
        angle_increment = 2 * math.pi / self.num_volcano_cards

        # Track the total number of cave segments generated
        total_cave_segments = 0

        # Create volcano cards around the chit cards forming a ring
        for i in range(self.num_volcano_cards):
            # Calculate the angle for the current volcano card
            angle = i * angle_increment

            # Calculate the position of the volcano card
            x = ring_center_x + int(radius * math.cos(angle))
            y = ring_center_y - int(radius * math.sin(angle))  # Reverse the y-coordinate to correctly position the cards

            # Determine the number of cave segments for this volcano card
            max_cave_segments = min(4, 4 - total_cave_segments)  # Ensure that the total number of cave segments does not exceed four
            segments = [random.choice([True, False]) for _ in range(max_cave_segments)]  # Randomly generate cave segments
            total_cave_segments += max_cave_segments  # Update the total number of cave segments

            # Create the volcano card
            volcano_card = VolcanoCard(x, y, 80, 20, segments)  # Increased width and height for better visibility
            self.volcano_cards.append(volcano_card)

        # Create chit cards in the center
        num_chit_cards = 16
        chit_card_width = 40
        chit_card_height = 60
        chit_card_spacing = 10
        for i in range(num_chit_cards):
            x = center_x - chit_card_width // 2 + (i % 4) * (chit_card_width + chit_card_spacing)
            y = center_y - chit_card_height // 2 + (i // 4) * (chit_card_height + chit_card_spacing)
            chit_card = ChitCard(x, y, chit_card_width, chit_card_height)
            self.chit_cards.append(chit_card)

    def draw_board(self, screen):
        # Fill the screen with white color
        screen.fill(WHITE)
        # Draw chit cards on the screen
        for chit_card in self.chit_cards:
            chit_card.draw(screen)

        # Draw volcano cards on the screen
        for volcano_card in self.volcano_cards:
            volcano_card.draw(screen)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fiery Dragons Game")
clock = pygame.time
