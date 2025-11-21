import json
import os

DATA_FOLDER = "data"
CHARACTER_FILE = os.path.join(DATA_FOLDER, "characters.json")


def load_characters():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    if not os.path.exists(CHARACTER_FILE):
        with open(CHARACTER_FILE, "w") as f:
            json.dump({"characters": []}, f, indent=4)

    with open(CHARACTER_FILE, "r") as f:
        return json.load(f)


def save_characters(data):
    with open(CHARACTER_FILE, "w") as f:
        json.dump(data, f, indent=4)
