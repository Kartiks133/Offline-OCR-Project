import json

def save_metadata(metadata, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

def load_metadata(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)