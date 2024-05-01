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

        self.flipped = False  # Initially, the card is not flipped

    def draw(self, screen):
        # Draw chit card
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)
        # Draw the card based on its current state (flipped or not)
        if self.flipped:
            # Draw the back of the card
            pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        else:
            # Draw the front of the card
            pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

    def flip(self):
        # Toggle the flipped state of the card
        self.flipped = not self.flipped

# Define class for Volcano Card
class VolcanoCard:
    def __init__(self, x, y, width, height, has_cave, angle, cave_image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.has_cave = has_cave
        self.angle = angle  # Angle relative to the center of the circle
        # Load and scale cave segment image
        cave_image = pygame.image.load(cave_image_path).convert_alpha()
        scaled_width = 40  # Adjust this value as needed
        scaled_height = 40  # Adjust this value as needed
        self.cave_image = pygame.transform.scale(cave_image, (scaled_width, scaled_height))

    def rotate(self):
        # Calculate tilt angle based on position along the circle
        tilt_angle = math.degrees(math.atan2(SCREEN_HEIGHT // 2 - self.y, SCREEN_WIDTH // 2 - self.x))
        # Create a surface for the card
        card_surface = pygame.Surface((self.width, self.height))
        card_surface.fill(WHITE)  # Fill with white color
        # Rotate the card surface
        rotated_card = pygame.transform.rotate(card_surface, tilt_angle)
        # Get the new rectangle after rotation
        self.rect = rotated_card.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        # Calculate position based on angle
        radius = 250  # Radius of the circle
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        self.x = center_x + int(radius * math.cos(self.angle))
        self.y = center_y - int(radius * math.sin(self.angle))
        # Calculate tilt angle based on position along the circle
        tilt_angle = math.degrees(math.atan2(center_y - self.y, center_x - self.x))

        # Draw volcano card
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)

        if self.has_cave:
            # Adjust the position to draw the cave image above the volcano card
            cave_x = self.x - self.cave_image.get_width() // 2 + self.width // 2
            cave_y = self.y - self.cave_image.get_height() - 10  # Adjust this value as needed
            # Draw cave segment image
            cave_image_rotated = pygame.transform.rotate(self.cave_image, tilt_angle)  # Rotate the image
            screen.blit(cave_image_rotated, (cave_x, cave_y))  # Draw the image
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

        # Paths to the custom cave images
        cave_images_paths = [r"Game\Assets\bat.jpg", r"Game\Assets\Spider.PNG", r"Game\Assets\pngtree.png", r"Game\Assets\dragon.jpg"]


        # Create volcano cards around the chit cards forming a ring
        for i in range(self.num_volcano_cards):
            # Determine if the volcano card has a cave segment
            has_cave = i in cave_indices

            # Calculate the angle for the current volcano card
            angle = i * angle_increment

            # Create the volcano card with a custom cave image
            volcano_card = VolcanoCard(0, 0, 80, 20, has_cave, angle, cave_images_paths[i % len(cave_images_paths)])
            self.volcano_cards.append(volcano_card)

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

    def draw_board(self, screen):
        # Fill the screen with white color
        screen.fill(WHITE)
        # Draw chit cards on the screen
        for chit_card in self.chit_cards:
            chit_card.draw(screen)
        # Rotate and draw volcano cards on the screen
        for volcano_card in self.volcano_cards:
            volcano_card.rotate()  # Rotate the volcano card
            volcano_card.draw(screen)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fiery Dragons Game")
clock = pygame.time.Clock()

# Create game board
game_board = GameBoard()
game_board.initialize_board()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the boundaries of any chit card
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for chit_card in game_board.chit_cards:
                if chit_card.x <= mouse_x <= chit_card.x + chit_card.width and \
                   chit_card.y <= mouse_y <= chit_card.y + chit_card.height:
                    # Flip the clicked chit card
                    chit_card.flip()

    # Draw the game board
    game_board.draw_board(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()