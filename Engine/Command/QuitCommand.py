import pygame
from Engine.Command import Command

class QuitCommand(Command):
    def run(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        