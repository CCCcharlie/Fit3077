import pygame
from Engine.Command import Command
from Engine.Scene import Scene
from Engine.World import World

class ChangeSceneCommand(Command):
    def __init__(self, newScene: Scene):
        self.newScene = newScene

    def run(self):
        World.getInstance().setActiveScene(self.newScene)
        
        