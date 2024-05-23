from typing import Dict, List

from engine.utils import SingletonMeta
from fieryDragons.save.FileDataHandler import FileDataHandler
from fieryDragons.save.Serializable import Serializable


class SaveManager(metaclass=SingletonMeta):
  def __init__(self):
    self.__serializables: Dict[str, Serializable] = {}
    self.__fileDataHandler: FileDataHandler = FileDataHandler()

  def register(self, s: Serializable):
    uuid: str = s.getUUID()
    if uuid in self.__serializables:
      raise ValueError(f"Cannot register. Serializable with uuid {uuid} already is registered")
    self.__serializables[uuid] = s

  def deregister(self, s: Serializable):
    uuid: str = s.getUUID()
    if uuid not in self.__serializables:
      raise ValueError(f"Cannot de register. Serializable with uuid {uuid} already is not registered")
    self.__serializables.pop(uuid)

  def save(self, saveId: int):
    jsonData = {}
    jsonData["seed"] = 0
    for uuid, s in self.__serializables.items():
      jsonData[uuid] = s.serialise()

    self.__fileDataHandler.save(saveId, jsonData)
    pass

  def load(self, saveId: int):
    pass
    
  
