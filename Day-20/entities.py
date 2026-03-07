from abc import ABC, abstractmethod
import random

class Entity(ABC):
    def __init__(self, name: str, health: int):
        self.name = name
        self._health = health  # Encapsulation

    @property
    def is_alive(self) -> bool:
        return self._health > 0

    @abstractmethod
    def attack(self) -> int:
        pass

    def take_damage(self, amount: int):
        self._health -= amount
        print(f"{self.name} took {amount} damage! Remaining HP: {max(0, self._health)}")