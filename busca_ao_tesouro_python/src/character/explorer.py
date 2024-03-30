
class Explorer:
    def __init__(self, max_health=100, max_attack=10):
        self.max_health = max_health  
        self.max_attack = max_attack  
        self.health = max_health      
        self.attack = max_attack      
        self.treasure_percentage = 100  
        self.weapon = None            
        self.checkpoints_found = []   

    def attack_enemy(self, enemy, weapon):
        if self.weapon:
            damage = self.attack + weapon.attack_bonus
        else:
            damage = self.attack
        enemy.take_damage(damage)

    def take_damage(self, damage):
       
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self):
        self.health +=20 #pontos fixos do bioma de chá
        if self.health > 100 :
            self.health = 100

    def carry_treasure(self):
       
        return self.treasure_percentage

    def equip_weapon(self, weapon):
        
        if self.weapon:
            print("Você já está com uma arma equipada.")
            return

        self.weapon = weapon
       
        self.treasure_percentage -= weapon.treasure_penalty

    def drop_weapon(self):
       
        self.weapon = None
