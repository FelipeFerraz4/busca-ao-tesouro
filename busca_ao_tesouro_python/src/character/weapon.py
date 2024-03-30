class Weapon:
    def __init__(self, attack_bonus, treasure_penalty, remaining_usage ):
        self.attack_bonus = attack_bonus 
        self.treasure_penalty = treasure_penalty  
        self.remaining_usage = remaining_usage

def use_weapon(self):
        
        if self.usos_restantes > 0:
            self.usos_restantes -= 1
            return self.usos_restantes
        else:
            return 0