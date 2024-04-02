import pygame

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, surface):
        action = False
        position = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(position) == True:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
def create_button_reset():
    start_img = pygame.image.load('./src/assets/button_image/reset_button.jpeg')
    start_img = pygame.transform.scale(start_img, (200, 200))
    return Button(800, 200, start_img)

def create_button_scape():
    start_img = pygame.image.load('./src/assets/image/scape_button.jpg')
    start_img = pygame.transform.scale(start_img, (200, 200))
    return Button(800, 400, start_img)

def create_button_release():
    start_img = pygame.image.load('./src/assets/button_image/release_button.jpeg')
    start_img = pygame.transform.scale(start_img, (200, 200))
    return Button(800, 400, start_img)

def create_button_next():
    start_img = pygame.image.load('./src/assets/image/next_button.jpeg')
    start_img = pygame.transform.scale(start_img, (200, 200))
    return Button(800, 200, start_img)

def create_button_combat():
    start_img = pygame.image.load('./src/assets/image/combat_button.jpg')
    start_img = pygame.transform.scale(start_img, (200, 200))
    return Button(800, 200, start_img)

def create_button_get():
    start_img = pygame.image.load('./src/assets/button_image/get_button.jpeg')
    start_img = pygame.transform.scale(start_img, (200, 200))
    return Button(800, 400, start_img)

def create_button_florest():
    start_img = pygame.image.load('./src/assets/button_image/florest_button.jpeg')
    start_img = pygame.transform.scale(start_img, (200, 200))
    return Button(800, 400, start_img)

