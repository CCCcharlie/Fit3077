from typing import Dict, List
import json
import os

class FileDataHandler:
  def __init__(self):
    self.__base_filename = "./saves/"
    if not os.path.exists(self.__base_filename):
      os.makedirs(self.__base_filename)

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
    
  def getAllSaves(self,) -> List[int]:
    """
    Finds the index of avaliable save files
    """
    save_files = []
    for filename in os.listdir(self.__base_filename):
        if filename.startswith("save_") and filename.endswith(".json"):
            try:
                save_id = int(filename[5:-5])
                save_files.append(save_id)
            except ValueError:
                # Skip files that don't have a proper integer saveId
                continue
    return sorted(save_files)

    