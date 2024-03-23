import pygame

class Biome():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def draw_biome(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
def create_biome():
    images = []
    biome = pygame.image.load('./src/assets/image/home_beach_biome.jpeg')
    biome = pygame.transform.scale(biome, (200, 200))
    return Biome(800, 0, biome)


def draw_biomes(biome, surface, type):
    biome.draw_biome(surface)