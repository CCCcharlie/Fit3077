import random
from typing import Any, List

from engine.utils.SingletonMeta import SingletonMeta 

class Random(metaclass = SingletonMeta):
  def __init__(self):
    self.seed: int = None
    self.__index = -1

  def generateSeed(self):
    self.__seed = random.randint(0,9999999)
    random.seed(self.__seed)
  
  def setSeed(self, seed: int):
    self.__seed = seed
    random.seed(self.__seed)

  def getSeed(self) -> int:
    return self.__seed
  

  def randint(a,b) -> int:
    return random.randint(a,b)
  
  def shuffle(self, list: List):
    """
    Shuffle in place and return none
    """
    random.shuffle(list)

  def choice(self, list: List[Any]) -> Any:
    if not list: 
      return None # return none if the list is empty 
    return random.choice(list)
  
  def getId(self)-> int:
    self.__index += 1
    return self.__index
