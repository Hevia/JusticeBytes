import json

def loadJSON(data_path: str) -> dict:
    try:
        with open(data_path) as json_data:
            data = json.load(json_data)
            return data
    except Exception:
        raise Exception(f"Could not open file located at: {data_path}")