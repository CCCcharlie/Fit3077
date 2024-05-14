from abc import ABC, abstractmethod
from typing import List

from engine.observer.subscriber import Subscriber
from engine.utils.SingletonMeta import SingletonMeta

class Emitter(ABC, metaclass=SingletonMeta):
    """
    Emitter than handles the notification of events
    
    Based on the observer pattern
    """
    def __init__(self):
        """
        Create the emitter class
        """
        self.__subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        """
        Subscribe to this emitters notifications

        Args:
            subscriber (Subscriber): The subscriber to add
        """
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        """
        Unsubscribe to this emitters notifications

        Args:
            subscriber (Subscriber): The subscriber to remove
        """
        self.__subscribers.remove(subscriber)

    def notify(self):
        """
        Notify subscribers that this event has occured
        """
        for subscriber in self.__subscribers:
            subscriber.notify()

    

