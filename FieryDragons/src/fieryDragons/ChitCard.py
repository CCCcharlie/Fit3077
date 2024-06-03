from enum import Enum
from typing import Dict, List

from engine.command.Command import Command
from engine.component.TransformComponent import TransformComponent
from engine.component.renderable.RenderableComponent import RenderableComponent
from engine.entity.Updateable import Updateable
from engine.observer.subscriber import Subscriber
from fieryDragons.observer.PlayerTurnEndEmitter import PlayerTurnEndEmitter
from engine.Serializable import Serializable

class State(Enum):
    HIDDEN = 1
    VISIBLE = 2

class ChitCard(Subscriber, Updateable, Serializable):
    def __init__(self, transforms: List[TransformComponent], front: List[RenderableComponent], back: RenderableComponent, command: Command):
        """
        
        Args:
            command (Command): The command to run when this chit card is flipped
        """
        self.__front: List[RenderableComponent] = front
        self.__back: RenderableComponent = back
        self.__state: State = State.HIDDEN
        self.__command: Command = command

        self.__transforms: List[TransformComponent] = transforms

        PlayerTurnEndEmitter().subscribe(self)

        self.__timer:float = -1
        self.__debug:bool = False

        for renderable in self.__front:
            
            renderable.hide()

        self.__transformData = []

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
                self.__command.run()
                

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
        d["transforms"] = [transform.serialise() for transform in self.__transforms]
        d["info"] = str(self.__command)
        return d
    
    def inPosition(self) -> None:
        if self.__state == State.VISIBLE:
            for renderable in self.__front:
                renderable.show()
            self.__back.hide()
        else:
            for renderable in self.__front:
                renderable.hide()
            self.__back.show()

        for (transform, data) in zip(self.__transforms, self.__transformData):
            transform.deserialise(data)
    
    def deserialise(self, data: Dict) -> None:
        print("loading chit card data " + str(self.__command))
        ## deserialise state 
        state = data["state"]
        self.__state = State(state)
        

        ## deserialise transforms
        self.__transformData = data["transforms"]
    
        

