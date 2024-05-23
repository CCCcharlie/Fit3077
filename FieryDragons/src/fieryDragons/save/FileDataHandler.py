from typing import Dict
import json

class FileDataHandler:
  def __init__(self):
    self.__base_filename = "/save/"

  def __getFilename(self, saveId: int) -> str:
    return f"{self.__base_filename}save_{saveId}.json"
  
  def save(self, saveId: int, jsonData: Dict) -> None:
    filename = self.__getFilename(saveId)

    with open(filename, 'w') as file:
      json.dump(jsonData, file, indent=4)
    

  def load(self, saveId: int) -> Dict:
    filename = self.__getFilename(saveId)

    try: 
      with open(filename, 'r') as file:
        data = json.load(file)
      return data
    except FileNotFoundError:
      raise ValueError(f"No data found for saveId {saveId}")
    