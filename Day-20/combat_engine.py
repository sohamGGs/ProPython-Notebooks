from entities import Entity

class Battle:
    def __init__(self, hero: Entity, monster: Entity):
        self.hero = hero
        self.monster = monster

    def start(self):
        print(f"\n--- BATTLE START: {self.hero.name} vs {self.monster.name} ---")
        round_count = 1
        
        while self.hero.is_alive and self.monster.is_alive:
            print(f"\n[Round {round_count}]")
            # Hero attacks Monster
            dmg = self.hero.attack()
            self.monster.take_damage(dmg)
            
            if not self.monster.is_alive:
                print(f"🏆 {self.monster.name} has been defeated!")
                break
                
            # Monster attacks Hero
            dmg = self.monster.attack()
            self.hero.take_damage(dmg)
            
            round_count += 1