
from Engine import *
from Game.Src.Components.ChitCardComponent import ChitCardComponent

"""
Simple implementation of a command that prints a string
used for testing of the command data structure
"""
class ChitCardClickedCommand(Command):
    def __init__(self, ccComponent: ChitCardComponent ):
        self.chitCard = ccComponent
        
    def run(self):
        print("chit card clicked")
        self.chitCard.onClick()