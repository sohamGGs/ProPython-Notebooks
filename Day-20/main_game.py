from heroes import Warrior, Mage
from entities import Entity
from combat_engine import Battle
import random

class Goblin(Entity):
    def attack(self):
        print(f"👹 Goblin lunges with a dagger!")
        return random.randint(5, 15)

if __name__ == "__main__":
    player_name = input("Enter Hero Name: ")
    choice = input("Choose Class (1: Warrior, 2: Mage): ")
    
    player = Warrior(player_name, 100) if choice == "1" else Mage(player_name, 80)
    enemy = Goblin("Evil Grunt", 60)
    
    game = Battle(player, enemy)
    game.start()