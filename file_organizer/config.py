import json
import os

def load_categories():
    base_dir = os.path.dirname(__file__)  # folder of config.py
    file_path = os.path.join(base_dir, "categories.json")

    with open(file_path, "r") as f:
        return json.load(f)