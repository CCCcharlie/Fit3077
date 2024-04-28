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
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height), 2)


# Define class for Volcano Card
class VolcanoCard:
    def __init__(self, x, y, radius, num_segments):
        self.x = x
        self.y = y
        self.radius = radius
        self.num_segments = num_segments

    def draw(self, screen):
        # Calculate the angle between each segment
        segment_angle = 2 * math.pi / self.num_segments
        
        # Draw volcano card segments
        for i in range(self.num_segments):
            start_angle = i * segment_angle
            end_angle = (i + 1) * segment_angle
            
            # Calculate the start and end points of each segment
            start_x = self.x + int(self.radius * math.cos(start_angle))
            start_y = self.y + int(self.radius * math.sin(start_angle))
            end_x = self.x + int(self.radius * math.cos(end_angle))
            end_y = self.y + int(self.radius * math.sin(end_angle))
            
            # Draw a line segment between the start and end points
            pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 2)
    def __init__(self, x, y, radius, num_segments):
        self.x = x
        self.y = y
        self.radius = radius
        self.num_segments = num_segments

    def draw(self, screen):
        # Draw volcano card segments
        segment_angle = 2 * math.pi / self.num_segments  # 每个段落的角度
        for i in range(self.num_segments):
            angle = i * segment_angle
            start_x = self.x + int(self.radius * math.cos(angle))
            start_y = self.y + int(self.radius * math.sin(angle))
            end_x = self.x + int(self.radius * math.cos(angle + segment_angle))
            end_y = self.y + int(self.radius * math.sin(angle + segment_angle))
            pygame.draw.line(screen, BLACK, (start_x, start_y), (end_x, end_y), 2)
    def __init__(self, x, y, radius, num_segments):
        self.x = x
        self.y = y
        self.radius = radius
        self.num_segments = num_segments

    def draw(self, screen):
        # Draw volcano card segments
        segment_angle = 360 / self.num_segments
        for i in range(self.num_segments):
            start_angle = i * segment_angle
            end_angle = (i + 1) * segment_angle
            pygame.draw.arc(screen, BLACK, (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2), math.radians(start_angle), math.radians(end_angle), 3)
    def __init__(self, x, y, radius, segments):
        self.x = x
        self.y = y
        self.radius = radius
        self.segments = segments

    def draw(self, screen):
        # Draw volcano card segments
        segment_angle = 360 / len(self.segments)
        for i, has_cave in enumerate(self.segments):
            if has_cave:
                color = BLACK  # Segment with cave
            else:
                color = WHITE  # Empty segment
            # Calculate segment start angle
            start_angle = i * segment_angle
            # Calculate segment end angle
            end_angle = start_angle + segment_angle
            # Draw segment arc
            pygame.draw.arc(screen, color, (self.x - self.radius, self.y - self.radius, 2*self.radius, 2*self.radius),
                            math.radians(start_angle), math.radians(end_angle), 3)

# Define class for GameBoard
class GameBoard:
    def __init__(self):
        self.volcano_cards = []
        self.num_volcano_cards = 8  # 火山卡数量

    def initialize_board(self):
        # Create volcano cards around the center forming a ring
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        radius = 200
        for i in range(self.num_volcano_cards):
            angle = i * (2 * math.pi / self.num_volcano_cards)
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            segments = 3  # 每个火山卡有三个段落
            volcano_card = VolcanoCard(x, y, 40, segments)
            self.volcano_cards.append(volcano_card)
    def __init__(self):
        self.volcano_cards = []

    def initialize_board(self):
        # Create volcano cards around the center
        num_volcano_cards = 8
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        radius = 200
        for i in range(num_volcano_cards):
            angle = i * (2 * math.pi / num_volcano_cards)
            x = center_x + int(radius * math.cos(angle))
            y = center_y + int(radius * math.sin(angle))
            segments = 3  # 每个火山卡有三个段落
            volcano_card = VolcanoCard(x, y, 40, segments)
            self.volcano_cards.append(volcano_card)
    def __init__(self):
        self.volcano_cards = []
        self.chit_cards = []

    def initialize_board(self):
        # Create volcano cards around the center
        num_volcano_cards = 8
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        radius = 200
        for i in range(num_volcano_cards):
            angle = i * (2 * math.pi / num_volcano_cards)  # 计算当前火山卡所在的角度
            x = center_x + int(radius * math.cos(angle))  # 根据角度计算 x 坐标
            y = center_y + int(radius * math.sin(angle))  # 根据角度计算 y 坐标
            segments = [random.choice([True, False]) for _ in range(3)]  # 随机生成火山卡的洞的分布情况
            volcano_card = VolcanoCard(x, y, radius, segments)  # 创建火山卡对象
            self.volcano_cards.append(volcano_card)  # 将火山卡添加到列表中

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
        # Draw volcano cards on the screen
        screen.fill(WHITE)
        for volcano_card in self.volcano_cards:
            volcano_card.draw(screen)
        # Draw chit cards on the screen
        for chit_card in self.chit_cards:
            chit_card.draw(screen)

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

    # Draw the game board
    game_board.draw_board(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
