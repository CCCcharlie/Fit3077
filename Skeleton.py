from Entity import Entity

class Skeleton(Entity):
    def __init__(self):
        super().__init__()
        self.patrollingLeft = False

    def update(self):
        if self.patrollingLeft:
            self.setX(self.x() - 1)
            if self.x() == 0:
                self.patrollingLeft = False
        else:
            self.setX(self.x() + 1)
            if self.x() == 100:
                self.patrollingLeft = True
      
    def render(self):
        print("rendering skeleton")
        pass 
