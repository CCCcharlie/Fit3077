from abc import abstractmethod
from typing import Dict
import random

class Serializable():
  """

  """
  def __init__(self):
     self.__uuid: str = str(random.randint(0,9999999))

  def getUUID(self) -> str:
     return self.__uuid
  
  @abstractmethod
  def serialise(self) -> Dict:
      """
      
      """
      raise NotImplementedError()
  
  @abstractmethod
  def deserialise(self, data: Dict) -> None:
     """
     """
     raise NotImplementedError()

  