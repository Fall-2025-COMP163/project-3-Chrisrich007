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
