from collections import defaultdict
from collections.abc import Mapping, MutableSet

from .game_objects import GameObject
from .interfaces import UpdateableInterface


class Scene(UpdateableInterface):

    def __init__(self) -> None:
        self._objects: Mapping[int, MutableSet[GameObject]] = defaultdict(set)

    def add_object(self, obj: GameObject, layer: int) -> None:
        self._objects[layer].add(obj)

    def remove_object(self, obj, layer: int | None = None) -> None:
        if layer is None:
            for layer_set in self._objects.values():
                try:
                    layer_set.remove(obj)
                except KeyError:
                    pass
        else:
            try:
                self._objects[layer].remove(obj)
            except KeyError:
                pass

    def update(self) -> None:
        sorted_layers = sorted(self._objects.items(), key=lambda x: x[0])
        for _, layer_set in sorted_layers:
            for layer_obj in layer_set:
                layer_obj.update()
