from src.graph.search import breadthFirstSearch, depthFirstSearch, searchVerticalEmpty
from src.config.button import *
from src.graph.read import graphRead
from src.graph.vertice import *
from src.config.screen import *
from src.graph.informateVertice import draw_informationVetices
from .draw_info_vertice import *
from src.character.monster import *
from src.character.weapon import *
from .display import *

import pygame
from time import sleep

screen = createScreen()
backGround = createBackground()
graph = graphRead()

pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 40)

button_reset = create_button_reset()
button_next = create_button_next()
button_scape = create_button_scape()
button_combat = create_button_combat()
button_get = create_button_get()
button_release = create_button_release()
button_florest = create_button_florest()

def displayStart(game, monsters, weapons):
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters, weapons)
    
    if game.statusGame == -1:
        txttela = fontesys.render('Prepare-se, a ilha está a vista', 1, (255,255,255))
    elif game.statusGame == -2:
        txttela = fontesys.render('Desvende segredos ocultos e tesouros.', 1, (255,255,255))
    elif game.statusGame == -3:
        txttela = fontesys.render('Uma jornada emocionante começa agora!', 1, (255,255,255))
    screen.blit(txttela, (180, 280))
    count_timer = pygame.time.get_ticks()
    if game.startTime + 1500 <= count_timer <= game.startTime + 2500:
        game.statusGame = -2
    elif game.startTime + 2500 < count_timer <= game.startTime + 3500:
        game.statusGame = -3
    elif game.startTime + 3500 < count_timer:
        game.statusGame =  0
        
def displayDefault(game, monsters, person, weapons):
    info_base(game, monsters, person, weapons)
    if button_next.draw(screen):
        passo(game)
        print('next')
        sleep(0.2)
    if button_florest.draw(screen):
        print('florest')
        
def displayEnd(game, monsters, person, weapons):
    info_base(game, monsters, person, weapons)
    if button_reset.draw(screen):
        reset(game)
        print('reset')
    if button_florest.draw(screen):
        print('florest')
        
def displayCombat(game, monsters, person, weapons):
    info_base(game, monsters, person, weapons)
    combat_mensagem(game)
    if button_combat.draw(screen):
        combat(game)
        print('combat')
    if button_scape.draw(screen):
        scape(game)
        print('scape')
        
def displayWeapon(game, monsters, person, weapons):
    info_base(game, monsters, person, weapons)
    if button_next.draw(screen):
        passo(game)
        game.statusGame = 0
        print('next')
    if button_get.draw(screen):
        get_weapon(game)
        print('weapon')
        
def info_base(game, monsters, person, weapons):
    global graph
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters, weapons)
    person.draw_explorer_info(fontesys, screen, weapons)
    txttela = fontesys.render(f'Passos: {game.time}', 1, (255,255,255))
    screen.blit(txttela, (0, 30))
    
def reset(game):
    game.time = 0
    game.statusGame = -1
    
def combat_mensagem(game):
    if game.combatRound == 3:
        txttela = fontesys.render('Monstro, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))
    elif game.combatRound == 2:
        txttela = fontesys.render('Segundo turno, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))
    elif game.combatRound == 1:
        txttela = fontesys.render('Terceiro turno, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))
        
def combat(game):
    print(game.statusGame)
    print(game.combatRound)
    if game.combatRound == 3:
        game.combatRound -= 1
    elif game.combatRound == 2:
        game.combatRound -= 1
    elif game.combatRound == 1:
        game.statusGame = 0
        game.combatRound = 3
        game.time += 1
        
def scape(game):
    game.time += 1
    game.statusGame = 0
    
def passo(game):
    game.time += 1
    
def get_weapon(game):
    game.time += 1
    game.statusGame = 0