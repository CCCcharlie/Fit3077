from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import MutableSequence
from .events import Event, ClickEvent
from .observer import ObserverInterface
import pygame
import sys


class EventHandler(ABC):

    def __init__(self) -> None:
        self.subscribers: MutableSequence[ObserverInterface] = []

    def add_subscriber(self, subscriber: ObserverInterface) -> EventHandler:
        self.subscribers.append(subscriber)
        return self

    def remove_subscriber(self, subscriber: ObserverInterface) -> EventHandler:
        self.subscribers.remove(subscriber)
        return self

    def _emit(self, event: Event) -> None:
        for subscriber in self.subscribers:
            subscriber.notify(event)


class PygameEventHandler(EventHandler):

    def __init__(self, event_type: int) -> None:
        super().__init__()
        self.event_type = event_type

    def handle_events(self) -> int:
        i = 0
        for event in pygame.event.get(self.event_type):
            i += 1
            self._emit(self.process_event(event))
        return i

    @classmethod
    @abstractmethod
    def get_instance(cls) -> PygameEventHandler:
        pass

    @abstractmethod
    def process_event(self, event: pygame.event.Event) -> Event:
        pass


class PygameQuitHandler(PygameEventHandler):

    instance: PygameQuitHandler | None = None

    def __init__(self) -> None:
        if PygameQuitHandler.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {PygameQuitHandler.__name__} more than once. Use get_instance()"
            )
        super().__init__(pygame.QUIT)

    @classmethod
    def get_instance(cls) -> PygameQuitHandler:
        if cls.instance is None:
            cls.instance = PygameQuitHandler()
        return cls.instance

    def handle_events(self) -> int:
        i = super().handle_events()
        if i > 0:
            pygame.quit()
            sys.exit(0)
        return i

    def process_event(self, event: pygame.event.Event) -> Event:
        return Event()


class PygameClickHandler(PygameEventHandler):
    instance: PygameClickHandler | None = None

    def __init__(self) -> None:
        if PygameClickHandler.instance is not None:
            raise ValueError(
                f"Cannot instantiate singleton {PygameClickHandler.__name__} more than once. Use get_instance()"
            )
        super().__init__(pygame.MOUSEBUTTONDOWN)

    @classmethod
    def get_instance(cls) -> PygameClickHandler:
        if cls.instance is None:
            cls.instance = PygameClickHandler()
        return cls.instance

    def process_event(self, event: pygame.event.Event) -> Event:
        return ClickEvent(event.pos[0], event.pos[1])
