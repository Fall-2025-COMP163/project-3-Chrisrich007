import character_manager
import inventory_system
import quest_handler
import combat_system
import game_data

# No runtime menu. This file exists so the imports resolve correctly.

from inventory_system import Inventory
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    CharacterDeadError,
)
import game_data


VALID_CLASSES = {"Warrior", "Mage", "Rogue"}


class Character:
    def __init__(self, name, role):
        if role not in VALID_CLASSES:
            raise InvalidCharacterClassError(f"Invalid class: {role}")

        self.name = name
        self.role = role
        self.hp = 100
        self.attack_power = 20
        self.inventory = Inventory()

    def is_alive(self):
        return self.hp > 0


class CharacterManager:
    def __init__(self):
        self.data = game_data.load_characters()

    def save(self):
        game_data.save_characters(self.data)

    def create_character(self, name, role):
        new_char = Character(name, role)
        self.data["characters"].append({
            "name": name,
            "role": role,
            "hp": new_char.hp,
            "inventory": []
        })
        self.save()
        return new_char

    def get_character(self, name):
        for entry in self.data["characters"]:
            if entry["name"] == name:
                char = Character(entry["name"], entry["role"])
                char.hp = entry["hp"]
                char.inventory.items = entry["inventory"]
                return char
        raise CharacterNotFoundError(f"Character '{name}' not found.")

    def update_character(self, character):
        for entry in self.data["characters"]:
            if entry["name"] == character.name:
                entry["hp"] = character.hp
                entry["inventory"] = character.inventory.items
                self.save()
                return
        raise CharacterNotFoundError(character.name)

class InvalidCharacterClassError(Exception):
    """Raised when a character is created with an unsupported class."""
    pass


class CharacterNotFoundError(Exception):
    """Raised when attempting to retrieve a character that does not exist."""
    pass


class CharacterDeadError(Exception):
    """Raised when an action is attempted on a dead character."""
    pass


class InventoryFullError(Exception):
    """Raised when trying to add an item to a full inventory."""
    pass


class ItemNotFoundError(Exception):
    """Raised when trying to remove or use an item that does not exist."""
    pass


class QuestNotFoundError(Exception):
    """Raised when a quest ID does not exist."""
    pass


class QuestAlreadyCompletedError(Exception):
    """Raised when trying to complete a quest that is already done."""
    pass


class InvalidEnemyError(Exception):
    """Raised when combat is attempted against an invalid enemy."""
    pass


from custom_exceptions import InventoryFullError, ItemNotFoundError


class Inventory:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.items = []

    def add_item(self, item):
        if len(self.items) >= self.max_size:
            raise InventoryFullError("Inventory is full.")
        self.items.append(item)

    def remove_item(self, item):
        if item not in self.items:
            raise ItemNotFoundError(f"Item '{item}' not found.")
        self.items.remove(item)

    def list_items(self):
        return self.items

from inventory_system import Inventory
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    CharacterDeadError,
)
import game_data


VALID_CLASSES = {"Warrior", "Mage", "Rogue"}


class Character:
    def __init__(self, name, role):
        if role not in VALID_CLASSES:
            raise InvalidCharacterClassError(f"Invalid class: {role}")

        self.name = name
        self.role = role
        self.hp = 100
        self.attack_power = 20
        self.inventory = Inventory()

    def is_alive(self):
        return self.hp > 0


class CharacterManager:
    def __init__(self):
        self.data = game_data.load_characters()

    def save(self):
        game_data.save_characters(self.data)

    def create_character(self, name, role):
        new_char = Character(name, role)
        self.data["characters"].append({
            "name": name,
            "role": role,
            "hp": new_char.hp,
            "inventory": []
        })
        self.save()
        return new_char

    def get_character(self, name):
        for entry in self.data["characters"]:
            if entry["name"] == name:
                char = Character(entry["name"], entry["role"])
                char.hp = entry["hp"]
                char.inventory.items = entry["inventory"]
                return char
        raise CharacterNotFoundError(f"Character '{name}' not found.")

    def update_character(self, character):
        for entry in self.data["characters"]:
            if entry["name"] == character.name:
                entry["hp"] = character.hp
                entry["inventory"] = character.inventory.items
                self.save()
                return
        raise CharacterNotFoundError(character.name)

from custom_exceptions import CharacterDeadError, InvalidEnemyError


class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0


class CombatSystem:
    def attack(self, character, enemy):
        if not character.is_alive():
            raise CharacterDeadError(f"{character.name} is dead and cannot fight.")
        if not isinstance(enemy, Enemy):
            raise InvalidEnemyError("Invalid enemy instance.")

        enemy.hp -= character.attack_power
        if enemy.is_alive():
            character.hp -= enemy.attack

        return {
            "character_hp": character.hp,
            "enemy_hp": enemy.hp,
        }
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

data/
   characters.json

{
    "characters": []
}
