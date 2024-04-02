import pygame
from src.graph.search import depthFirstSearch

class InfoVertice():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def draw_InfoVertice(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

def create_biome():
    biome = pygame.image.load('./src/assets/biome-img/safe_biome.jpeg')
    biome = pygame.transform.scale(biome, (200, 200))
    return InfoVertice(800, 0, biome)
   
def create_biome_0():
    biome = pygame.image.load('./src/assets/image/home_beach_biome.jpeg')
    biome = pygame.transform.scale(biome, (200, 200))
    return InfoVertice(800, 0, biome)

def create_biome_1():
    biome = pygame.image.load('./src/assets/biome-img/carnivorus_plant_biome.jpg')
    biome = pygame.transform.scale(biome, (200, 200))
    return InfoVertice(800, 0, biome)

def create_biome_2():
    biome = pygame.image.load('./src/assets/biome-img/healing_plant_biome1.jpeg')
    biome = pygame.transform.scale(biome, (200, 200))
    return InfoVertice(800, 0, biome)

def create_biome_3():
    biome = pygame.image.load('./src/assets/biome-img/poisonous_plant_biome.jpg')
    biome = pygame.transform.scale(biome, (200, 200))
    return InfoVertice(800, 0, biome)

def create_biome_4():
    biome = pygame.image.load('./src/assets/biome-img/rock_slide_biome.jpeg')
    biome = pygame.transform.scale(biome, (200, 200))
    return InfoVertice(800, 0, biome)

def create_biome_5():
    biome = pygame.image.load('./src/assets/biome-img/swamp_biome.jpg')
    biome = pygame.transform.scale(biome, (200, 200))
    return InfoVertice(800, 0, biome)

def create_biome_treasure():
    biome = pygame.image.load('./src/assets/image/treasure.jpeg')
    biome = pygame.transform.scale(biome, (200, 200))
    return InfoVertice(800, 0, biome)

def create_monster_ant():
   animal = pygame.image.load('./src/assets/animals-img/ant.jpeg')
   animal = pygame.transform.scale(animal, (200, 200))
   return InfoVertice(800, 0, animal)

def create_monster_jaguar():
   animal = pygame.image.load('./src/assets/animals-img/ounce.jpeg')
   animal = pygame.transform.scale(animal, (200, 200))
   return InfoVertice(800, 0, animal)

def create_monster_hawk():
   animal = pygame.image.load('./src/assets/animals-img/hawk.jpeg')
   animal = pygame.transform.scale(animal, (200, 200))
   return InfoVertice(800, 0, animal)

def create_monster_alligator():
   animal = pygame.image.load('./src/assets/animals-img/alligator.jpeg')
   animal = pygame.transform.scale(animal, (200, 200))
   return InfoVertice(800, 0, animal)

def create_weapon_bow():
   animal = pygame.image.load('./src/assets/weapon/bow.jpeg')
   animal = pygame.transform.scale(animal, (200, 200))
   return InfoVertice(800, 0, animal)

def create_weapon_dagger():
   animal = pygame.image.load('./src/assets/weapon/dagger.jpeg')
   animal = pygame.transform.scale(animal, (200, 200))
   return InfoVertice(800, 0, animal)

def create_weapon_gun():
   animal = pygame.image.load('./src/assets/weapon/gun.jpeg')
   animal = pygame.transform.scale(animal, (200, 200))
   return InfoVertice(800, 0, animal)

def create_weapon_sword():
   animal = pygame.image.load('./src/assets/weapon/sword.jpeg')
   animal = pygame.transform.scale(animal, (200, 200))
   return InfoVertice(800, 0, animal)
