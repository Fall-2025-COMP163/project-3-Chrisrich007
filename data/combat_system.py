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
