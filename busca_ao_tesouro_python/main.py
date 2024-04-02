import pygame
from pygame import mixer
from pygame.locals import *

from src.config.game import Game, gameOn
from src.character.explorer import Explorer
from src.character.monsterRead import monsterRead
from src.character.weaponRead import weaponsRead
from src.graph.read import graphRead

pygame.init()

run = True

#statusGame code 0 - continue, 1 - change goal, 2 - finish game, 3 - reset 
game = Game()
person = Explorer()
monsters = monsterRead()
weapon = weaponsRead()
graph = graphRead()

while run:
    gameOn(game, person, monsters, weapon, graph)
    
    if game.end == True:
        weapon = weaponsRead()
        graph = graphRead()
        monsters = monsterRead()
        person = Explorer()
        game = Game()

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()