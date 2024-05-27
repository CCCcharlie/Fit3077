from typing import Dict, List
import json
import os

from fieryDragons.save.FileDataHandler import FileDataHandler

class JsonDataHandler(FileDataHandler):

  def __getFilename(self, saveId: int) -> str:
    return f"{self._base_filename}save_{saveId}.json"
  
  def save(self, saveId: int, jsonData: Dict) -> None:
    """
    Save the current dictionary as save id into a json file

    Args:
      saveId (int): the id of the save
      data (Dict): The data to save
    """
    filename = self.__getFilename(saveId)

    with open(filename, 'w') as file:
      json.dump(jsonData, file, indent=4)
    
  def load(self, saveId: int) -> Dict:
    """
    Load the json save file into a dict
    
    Args:
      saveId (int): the dave id to load
    """
    filename = self.__getFilename(saveId)

    try: 
      with open(filename, 'r') as file:
        data = json.load(file)
      return data
    except FileNotFoundError:
      raise ValueError(f"No data found for saveId {saveId}")
    
  def getAllSaves(self) -> List[int]:
    """
    Finds the index of available save files
    """
    save_files = []
    for filename in os.listdir(self._base_filename):
        if filename.startswith("save_") and filename.endswith(".json"):
            try:
                save_id = int(filename[5:-5])
                save_files.append(save_id)
            except ValueError:
                # Skip files that don't have a proper integer saveId
                continue
    return sorted(save_files)

    