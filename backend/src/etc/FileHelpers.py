import json
import pickle

def loadJSON(data_path: str) -> dict:
    try:
        with open(data_path) as json_data:
            data = json.load(json_data)
            return data
    except Exception:
        raise Exception(f"Could not open file located at: {data_path}")

def load_file_as_list(file_path: str) -> str:
    """
    Loads the file at a specificed path, returns an error otherwise
        
    :param file_path (str): The path to the file you want to load
    :return _file a str of the contents of the file
    """
    _file = ""
    try:
        with open(file_path, "r") as fp:
            _file = fp.readlines()
        return _file
    except Exception:
        raise Exception(f"Error reading file at: {file_path}")

# Unpickles a file and returns the object
def unpickle(filename: str) -> object:
   pickleIn = open(filename, "rb")
   pickledObject = pickle.load(pickleIn)
   pickleIn.close()
   return pickledObject