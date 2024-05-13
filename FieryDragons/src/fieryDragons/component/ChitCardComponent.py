from enum import Enum
from engine.component.renderable.RenderableComponent import RenderableComponent
from subscriber import Subscriber

class State(Enum):
    HIDDEN = 1
    VISIBLE = 2

class ChitCard(Subscriber):
    def __init__(self, front: RenderableComponent, back: RenderableComponent):
        self.__front = front
        self.__back = back
        self.__state = State.HIDDEN

    def update(self, message):
        print(f"Chit Card received message: {message}")

    def onClick(self):
        if self.__state == State.HIDDEN:
            self.__state = State.VISIBLE
            self.__front.show()
            self.__back.hide()
            #  move player 

    def onHide(self):
        self.__state = State.HIDDEN
        self.__front.hide()
        self.__back.show()
