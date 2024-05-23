from enum import Enum
from typing import Dict, List

from engine.component.renderable.RenderableComponent import RenderableComponent
from engine.entity.Updateable import Updateable
from engine.observer.subscriber import Subscriber
from fieryDragons.command.MoveActivePlayerCommand import MoveActivePlayerCommand
from fieryDragons.enums.AnimalType import AnimalType
from fieryDragons.observer.PlayerTurnEndEmitter import PlayerTurnEndEmitter
from fieryDragons.save.Serializable import Serializable

class State(Enum):
    HIDDEN = 1
    VISIBLE = 2

class ChitCard(Subscriber, Updateable, Serializable):
    def __init__(self, front: List[RenderableComponent], back: RenderableComponent, animalType: AnimalType, amount: int):
        self.__front: List[RenderableComponent] = front
        self.__back: RenderableComponent = back
        self.__state: State = State.HIDDEN
        self.__animalType: AnimalType = animalType
        self.__amount: int = amount

        PlayerTurnEndEmitter().subscribe(self)

        self.__timer:float = -1
        self.__debug:bool = False

        for renderable in self.__front:
            renderable.hide()

        super().__init__()

    def activateDebug(self):
        self.__debug = True

    def onClick(self):
        
        if self.__state == State.HIDDEN:
            self.__state = State.VISIBLE
            for renderable in self.__front:
                renderable.show()
            self.__back.hide()
  
            if self.__debug is False:
                # move player
                MoveActivePlayerCommand(self.__animalType, self.__amount).run()

    def notify(self):
        if self.__state == State.VISIBLE:
            self.__timer = 1000
            self.__state = State.HIDDEN
            
    def onHide(self):
        
        for renderable in self.__front:
            renderable.hide()
        self.__back.show()
       
    def update(self, dt: float):
        if self.__timer > 0:
            self.__timer -= dt
            if self.__timer < 0:
                self.__timer = -1
                self.onHide()

    def serialise(self) -> Dict:
        d: dict = {}
        d["state"] = self.__state.value
        return d
    
    
    def deserialise(self, data: Dict) -> None:
        print(f"State is {data["state"]}")
        return 

