
from Engine import Command

"""
example command code from:
https://www.patternsgameprog.com/discover-python-and-patterns-20-better-commands
"""
class MoveCommand(Command):
    def __init__(self,state,unit,moveVector):
        self.state = state
        self.unit = unit
        self.moveVector = moveVector
        
    def run(self):
        # Update unit orientation
        if self.moveVector.x < 0: 
            self.unit.orientation = 90
        elif self.moveVector.x > 0: 
            self.unit.orientation = -90
        if self.moveVector.y < 0: 
            self.unit.orientation = 0
        elif self.moveVector.y > 0: 
            self.unit.orientation = 180

        # Compute new tank position
        newPos = self.unit.position + self.moveVector

        # Don't allow positions outside the world
        if newPos.x < 0 or newPos.x >= self.state.worldWidth \
        or newPos.y < 0 or newPos.y >= self.state.worldHeight:
            return

        # Don't allow wall positions
        if not self.state.walls[int(newPos.y)][int(newPos.x)] is None:
            return

        # Don't allow other unit positions 
        for otherUnit in self.state.units:
            if newPos == otherUnit.position:
                return

        self.unit.position = newPos