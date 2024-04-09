
from Engine.Command import Command

"""
Simple implementation of a command that prints a string
used for testing of the command data structure
"""
class PrintCommand(Command):
    def __init__(self,string):
        self.string = string
        
    def run(self):
        print(self.string)