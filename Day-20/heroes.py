from entities import Entity
import random

class Warrior(Entity):
    def attack(self) -> int:
        damage = random.randint(15, 25)
        print(f"⚔️ {self.name} swings a heavy sword!")
        return damage

class Mage(Entity):
    def attack(self) -> int:
        damage = random.randint(10, 40) # High variance
        print(f"🔥 {self.name} casts a Fireball!")
        return damage