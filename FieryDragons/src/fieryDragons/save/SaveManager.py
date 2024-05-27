from typing import Dict, List

from engine.utils import SingletonMeta
from fieryDragons.Random import Random
from fieryDragons.save.FileDataHandler import FileDataHandler
from fieryDragons.save.JsonDataHandler import JsonDataHandler
from fieryDragons.save.Serializable import Serializable


class SaveManager(metaclass=SingletonMeta):
  def __init__(self):
    self.__serializables: Dict[str, Serializable] = {}
    self.__fileDataHandler: FileDataHandler = JsonDataHandler()

  def register(self, s: Serializable):
    uuid: str = s.getUUID()
    if uuid in self.__serializables:
      pass
      raise ValueError(f"Cannot register. Serializable with uuid {uuid} already is registered")
    self.__serializables[uuid] = s

  def deregister(self, s: Serializable):
    uuid: str = s.getUUID()
    if uuid not in self.__serializables:
      raise ValueError(f"Cannot de register. Serializable with uuid {uuid} already is not registered")
    self.__serializables.pop(uuid)

  def save(self, saveId: int):
    jsonData = {}
    jsonData["seed"] = Random().getSeed()
    for uuid, s in self.__serializables.items():
      jsonData[uuid] = s.serialise()

    self.__fileDataHandler.save(saveId, jsonData)
    pass

  def load(self, saveId: int):
    data = self.__fileDataHandler.load(saveId)
    data.pop("seed")

    for uuid, s in self.__serializables.items():
      instanceData: Dict = data.get(uuid)
      s.deserialise(instanceData)

  def getSeed(self, saveId: int) -> int:
    data = self.__fileDataHandler.load(saveId)
    return data.get("seed")

  def onCleanup(self):
    self.__serializables = {}

  def getAllSaves(self) -> List[int]:
    """
    Finds the index of available save files 
    """
    return self.__fileDataHandler.getAllSaves()


  
