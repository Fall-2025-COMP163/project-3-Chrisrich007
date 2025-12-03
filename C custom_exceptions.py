"""
COMP 163 - Project 3: Quest Chronicles
Custom Exception Definitions

This module defines all custom exceptions used throughout the game.
"""

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

