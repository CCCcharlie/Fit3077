import pygame
import sys
import random
from entities.button import Button
from entities.gameboard import GameBoard
from entities.chitcard import ChitCard

def shuffle_all_cards():
    # Shuffle volcano cards
    gameboard.shuffle_volcano_cards()
    # Re-shuffle ChitCard details
    random.shuffle(card_details)
    # Re-initialize ChitCards with the new random order
    global chit_cards  # Use global to modify the existing chit_cards list
    chit_cards = [ChitCard(animal_type, count, i) for i, (animal_type, count) in enumerate(card_details)]

def draw_player_turn(surface, player_number):
    text = f"Player {player_number}'s Turn"
    text_surface = font.render(text, True, (255, 255, 255))  # White text
    surface.blit(text_surface, (10, 10))

def changeturn():
    global current_player  # Use global to modify the variable outside of the local scope
    current_player += 1  # Move to the next player
    if current_player > 4:  # If it goes beyond Player 4, wrap it back to Player 1
        current_player = 1

# Initialize Pygame
pygame.init()
pygame.font.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fiery Dragon Game")

font_size = 24
font = pygame.font.Font(None, font_size)



current_player = 1

# Initialize the gameboard
gameboard = GameBoard(8)

# Create a button that shuffles all cards when clicked
start_button = Button("Start", 650, 50, 100, 50, shuffle_all_cards)
change_turn_button = Button("Change Turn", 650, 150, 100, 50, changeturn)

# ChitCard details and positions
card_details = [
    ('Salamander', 1), ('Salamander', 2), ('Salamander', 3),
    ('Bat', 1), ('Bat', 2), ('Bat', 3),
    ('Spider', 1), ('Spider', 2), ('Spider', 3),
    ('Baby Dragon', 1), ('Baby Dragon', 2), ('Baby Dragon', 3),
    ('Pirate Dragon', 1), ('Pirate Dragon', 1),  # Two 1x Pirate Dragons
    ('Pirate Dragon', 2), ('Pirate Dragon', 2)   # Two 2x Pirate Dragons
]

# Initially shuffle and initialize ChitCards
random.shuffle(card_details)
chit_cards = [ChitCard(animal_type, count, i) for i, (animal_type, count) in enumerate(card_details)]

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        start_button.handle_event(event)  # Handle button events
        change_turn_button.handle_event(event)
    # Clear screen
    screen.fill((0, 0, 0))  # Fill screen with black or any other background color

    # Draw game elements
    for card in gameboard.cards:
        card.draw(screen)
    for chit_card in chit_cards:
        chit_card.draw(screen)
    start_button.draw(screen)
    change_turn_button.draw(screen)

    # Draw the current player's turn
    draw_player_turn(screen, current_player)

    # Update the display
    pygame.display.update()

    # Cap the frame rate to 60 FPS
    clock.tick(60)