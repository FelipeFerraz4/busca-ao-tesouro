import pygame
from pygame import mixer
from pygame.locals import *

from src.graph.read import graphRead
from src.config.screen import *
from src.config.button import *

pygame.init()

screen = createScreen()
backGround = createBackground()
graph = graphRead()
button_start = create_button_start()

run = True

while run:
    draw_backGround(graph, backGround, screen, button_start)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()