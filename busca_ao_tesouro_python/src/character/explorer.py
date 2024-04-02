from src.config.game import fontesys, graph, screen

class Explorer:
    def __init__(self, max_health=100, max_attack=10):
        self.max_health = max_health  
        self.max_attack = max_attack  
        self.health = max_health      
        self.attack = max_attack      
        self.treasure_percentage = 0  
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
        self.health += 20 #pontos fixos do bioma de chá
        if self.health > 100 :
            self.health = 100

    # def carry_treasure(self):
       
    #     return self.treasure_percentage

    def equip_weapon(self, weapon):
        
        if self.weapon:
            print("Você já está com uma arma equipada.")
            return

        self.weapon = weapon
       
        self.treasure_percentage -= weapon.treasure_penalty

    def drop_weapon(self):
       
        self.weapon = None

    def draw_explorer_info(self, fontesys, screen, weapons):
        txttela = fontesys.render(f'Ponto de vida: {self.health}', 1, (255,255,255))
        screen.blit(txttela, (0, 0))
        txttela = fontesys.render(f'Tesouro: {self.treasure_percentage}%', 1, (255,255,255))
        screen.blit(txttela, (270, 0))
        if self.weapon == None:
            txttela = fontesys.render(f'Arma: ', 1, (255,255,255))
        else:
            txttela = fontesys.render(f'Arma: {weapons[self.weapon].name}', 1, (255,255,255))
        screen.blit(txttela, (480, 0))
    
    def get_treasure(self, graph, vertice, weapons):
        if graph[vertice].treasure:
            self.treasure_percentage = self.health
            if self.weapon != None:
                self.treasure_percentage -= weapons[self.weapon].attack_bonus