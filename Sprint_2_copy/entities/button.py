import pygame

class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.callback = callback
        self.font = pygame.font.Font(None, 40)  # None defaults to the default font

    def draw(self, screen):
        # Draw the button rectangle
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
        # Render the text
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
                self.callback()