from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import MutableSequence
from typing import Type
from .events import Event, PygameEvent
from .observer import ObserverInterface
import pygame


class EventHandler(ABC):

    subscribers: MutableSequence[ObserverInterface] = []

    def __init__(self) -> None:
        raise ValueError(
            "Cannot instantiate an EventHandler, intended for static use only"
        )

    @classmethod
    def add_subscriber(cls, subscriber: ObserverInterface) -> Type["EventHandler"]:
        cls.subscribers.append(subscriber)
        return cls

    @classmethod
    def remove_subscriber(cls, subscriber: ObserverInterface) -> Type["EventHandler"]:
        cls.subscribers.remove(subscriber)
        return cls

    @classmethod
    def _emit(cls, event: Event) -> None:
        for subscriber in cls.subscribers:
            subscriber.notify(event)


class PygameEventHandler(EventHandler):

    @classmethod
    def emit(cls, event_type: int) -> int:
        i = 0
        for _ in pygame.event.get(event_type):
            i += 1
            cls._emit(PygameEvent(event_type))
        return i

    @classmethod
    @abstractmethod
    def handle_events(cls) -> None:
        pass


class PygameQuitHandler(PygameEventHandler):

    @classmethod
    def handle_events(cls) -> None:
        if cls.emit(pygame.QUIT) > 0:
            pygame.quit()
            exit(0)
