import pygame
import random
import math

# Define constants for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)

# Define class for Volcano Card
class VolcanoCard:
    def __init__(self, x, y, width, height, has_cave, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.has_cave = has_cave
        self.angle = angle  # Angle relative to the center of the circle

    def draw(self, screen):
        # Calculate position based on angle
        radius = 250  # Radius of the circle
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        self.x = center_x + int(radius * math.cos(self.angle))
        self.y = center_y - int(radius * math.sin(self.angle))

        # Draw volcano card
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)
        if self.has_cave:
            # Draw cave segment with outline
            # Adjusting position to place the cave segment at the volcano card's top center
            cave_x = self.x + self.width // 2 - min(self.width, self.height) // 4
            cave_y = self.y - min(self.width, self.height) // 4
            # pygame.draw.rect(screen, BLACK, (cave_x + 2, cave_y + 2, self.width - 4, self.height - 4), 2)
            circle_x = self.x + self.width // 2
            circle_y = self.y - min(self.width, self.height) // 2
            pygame.draw.circle(screen, BLACK, (circle_x, circle_y), min(self.width, self.height) // 4, 2)
        else:
            # Draw outline for empty segment
            pygame.draw.rect(screen, BLACK, (self.x + 2, self.y + 2, self.width - 4, self.height - 4), 2)

        # Draw dividing lines between segments
        num_segments = 4
        segment_width = self.width // num_segments
        for i in range(1, num_segments):
            pygame.draw.line(screen, BLACK, (self.x + i * segment_width, self.y), (self.x + i * segment_width, self.y + self.height), 2)

# Define class for GameBoard
class GameBoard:
    def __init__(self):
        self.volcano_cards = []
        self.chit_cards = []
        self.num_volcano_cards = 8  # Number of volcano cards
        self.num_caves = 4  # Number of cave segments across all volcano cards
        self.chit_card_width = 40  # Width of chit card
        self.chit_card_height = 60  # Height of chit card

    def initialize_board(self):
        # Calculate the angle increment for each volcano card
        angle_increment = 2 * math.pi / self.num_volcano_cards

        # Distribute cave segments across volcano cards
        cave_indices = random.sample(range(self.num_volcano_cards), self.num_caves)

        # Create volcano cards around the chit cards forming a ring
        for i in range(self.num_volcano_cards):
            # Determine if the volcano card has a cave segment
            has_cave = i in cave_indices

            # Calculate the angle for the current volcano card
            angle = i * angle_increment

            # Create the volcano card
            volcano_card = VolcanoCard(0, 0, 80, 20, has_cave, angle)
            self.volcano_cards.append(volcano_card)

            # # Adjusting position to place chit cards at the center of volcano cards
            # chit_card_x = volcano_card.x + volcano_card.width // 2 - self.chit_card_width // 2
            # chit_card_y = volcano_card.y + volcano_card.height // 2 - self.chit_card_height // 2
            # chit_card = ChitCard(chit_card_x, chit_card_y, self.chit_card_width, self.chit_card_height)
            # self.chit_cards.append(chit_card)
            # Create chit cards in the center
            center_x = SCREEN_WIDTH // 2
            center_y = SCREEN_HEIGHT // 2
            num_chit_cards = 16
            chit_card_width = 40
            chit_card_height = 60
            chit_card_spacing = 10
            # Calculate the total width and height of all chit cards
            total_width = (chit_card_width + chit_card_spacing) * 4 - chit_card_spacing
            total_height = (chit_card_height + chit_card_spacing) * (num_chit_cards // 4) - chit_card_spacing

            # Calculate the top left corner coordinates to center the chit cards
            start_x = (SCREEN_WIDTH - total_width) // 2
            start_y = (SCREEN_HEIGHT - total_height) // 2

            for i in range(num_chit_cards):
                # Calculate the x and y coordinates based on the index
                x = start_x + (i % 4) * (chit_card_width + chit_card_spacing)
                y = start_y + (i // 4) * (chit_card_height + chit_card_spacing)
                chit_card = ChitCard(x, y, chit_card_width, chit_card_height)
                self.chit_cards.append(chit_card)
                        # Calculate the total width and height of all VolcanoCards
            total_width_volcano = max([card.width for card in self.volcano_cards])
            total_height_volcano = max([card.height for card in self.volcano_cards]) * len(self.volcano_cards)

            # Calculate the top left corner coordinates to center the VolcanoCards
            start_x_volcano = (SCREEN_WIDTH - total_width_volcano) // 2
            start_y_volcano = (SCREEN_HEIGHT - total_height_volcano) // 2

            for volcano_card in self.volcano_cards:
                volcano_card.x = start_x_volcano
                volcano_card.y = start_y_volcano
                start_y_volcano += volcano_card.height



    def draw_board(self, screen):
        # Fill the screen with white color
        # Fill the screen with white color
        screen.fill(WHITE)
        # Draw chit cards on the screen
        for chit_card in self.chit_cards:
            chit_card.draw(screen)

        # Draw volcano cards on the screen
        for volcano_card in self.volcano_cards:
            volcano_card.draw(screen)

        # Draw volcano cards on the screen
        for volcano_card in self.volcano_cards:
            volcano_card.draw(screen)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fiery Dragons Game")
clock = pygame.time
