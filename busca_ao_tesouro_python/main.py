import pygame
from pygame import mixer
from pygame.locals import *

from src.config.game import Game, gameOn
from src.character.explorer import Explorer
from src.character.monsterRead import monsterRead
from src.character.weaponRead import weaponsRead

pygame.init()

run = True

#statusGame code 0 - continue, 1 - change goal, 2 - finish game, 3 - reset 
game = Game()
person = Explorer()
monsters = monsterRead()
weapon = weaponsRead()

while run:
    gameOn(game, person, monsters, weapon)
    
    # if game.statusGame == 1:
    #     game.verticeObjective = 10
    #     print('Change Goal')
    # if game.statusGame == 2:
    #     game.end = True
    # if game.statusGame == 3:
    #     game.verticeObjective = 3
    #     game.end = False
    #     game.statusGame = -1
    #     game.startTime = pygame.time.get_ticks()
    #     game.time = 0
    #     person.health = 100
    #     person.treasure_percentage = 0
    #     weapon = weaponsRead()
    #     person.weapon = None
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()