from time import sleep
import pygame
from pygame.locals import *
import random
import copy

from src.graph.search import breadthFirstSearch, depthFirstSearch, searchVerticalEmpty
from src.config.button import *
from src.graph.read import graphRead
from src.graph.vertice import *
from src.config.screen import *
from src.graph.informateVertice import draw_informationVetices
from .draw_info_vertice import *
from src.character.monster import *
from src.character.weapon import *

screen = createScreen()
backGround = createBackground()
graph = graphRead()

button_reset = create_button_reset()
button_next = create_button_next()
button_scape = create_button_scape()
button_combat = create_button_combat()
button_get = create_button_get()
button_release = create_button_release()

pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 40)

class Game():
    def __init__(
        self, 
        verticeObjective=3, 
        time=0, 
        startTime=pygame.time.get_ticks(), 
        statusGame=-1, 
        end=False,
        combatMenu=False,
        weaponMenu=False
        ):
      self.verticeObjective = verticeObjective
      self.time = time
      self.startTime = startTime
      self.statusGame = statusGame
      self.end = end
      self.combatMenu = combatMenu
      self.combatRound = 3
      self.weaponMenu = weaponMenu

def gameOn(game, person, monsters, weapons):
    if game.statusGame > -1:
        res = 0
        
        personVertice = depthFirstSearch(graph, graph[0])
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        if isSavePoint(graph, personVertice):
            person.checkpoints_found = personVertice
            graph[personVertice].savePoint = False
            
        if person.health <= 0 and person.checkpoints_found != -1:
            resurrect(person, graph, personVertice, weapons)
            if person.treasure_percentage >= 0:
                game.verticeObjective = 3
                person.treasure_percentage = 0

        
        if isMonster(monsters, personVertice):
            game.combatMenu = True
            game.startTime = pygame.time.get_ticks()
            
        if isWeapon(weapons, personVertice):
            game.weaponMenu = True
        
        if game.combatMenu == False and game.weaponMenu == False:
            res =  display_default(game, monsters, person, weapons)
        elif game.combatMenu == False and game.weaponMenu == True:
            res = display_weapon(game, monsters, person, weapons)
        else:
            res = display_combat(game, monsters, person, weapons)
        
        if res != 0:
            return res
        
        return message_end(game, person, nextVertice)
    else:
        return startMessage(game.statusGame, game.startTime, monsters, weapons)
    

def nextPosition(personVertice, verticeObjective):
    # get the best neighbor of the character's current vertice
    bestNeighboringVertice = breadthFirstSearch(graph, graph[personVertice], graph[verticeObjective])
    neighboringList = copy.deepcopy(graph[personVertice].adjacentVertices)
    
    # 20% of being chosen the best vertice
    porcente = 5/10
    luckNumber = random.randint(0, len(neighboringList))

    # choosing the next vertice
    neighboringChoice = bestNeighboringVertice
    
    if luckNumber > int(len(neighboringList)*porcente):
        if bestNeighboringVertice in neighboringList:
            neighboringList.remove(bestNeighboringVertice)
        numberChoice = random.randint(0, len(neighboringList) - 1)
        neighboringChoice = neighboringList[numberChoice]
    
    return neighboringChoice

def step(personVertice, nextVertice):
    #change the person's vertice
    graph[personVertice].person = False
    graph[nextVertice].person = True
    
def startMessage(statusGame, startTime, monsters, weapons):
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters, weapons)
    
    if statusGame == -1:
        txttela = fontesys.render('Prepare-se, a ilha está a vista', 1, (255,255,255))
    elif statusGame == -2:
        txttela = fontesys.render('Desvende segredos ocultos e tesouros.', 1, (255,255,255))
    elif statusGame == -3:
        txttela = fontesys.render('Uma jornada emocionante começa agora!', 1, (255,255,255))
    screen.blit(txttela, (180, 280))
    count_timer = pygame.time.get_ticks()
    if startTime + 1000 <= count_timer <= startTime + 2000:
        return -2
    elif startTime + 2000 < count_timer <= startTime + 3000:
        return -3
    elif startTime + 3000 < count_timer:
        return 0
    return -1

def display_default(game, monsters, person, weapons):
    global graph
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters, weapons)
    person.draw_explorer_info(fontesys, screen, weapons)
    personVertice = depthFirstSearch(graph, graph[0])
    
    person.get_treasure(graph, personVertice, weapons)
    
    if game.end == True:
        if button_reset.draw(screen):
            graph = graphRead()
            sleep(0.1)
            return 3
    elif person.weapon != None:
        if button_release.draw(screen):
            weapons[person.weapon].vertices = personVertice
            person.weapon = None
            
            nextVertice = nextPosition(personVertice, game.verticeObjective)
            step(personVertice, nextVertice)
            if nextVertice == 3:
                return 1
            game.time += 1
            damage_biome(graph, nextVertice, person, weapons)
            moviment_monster(graph, monsters, weapons)
            sleep(0.2)
            
    if button_next.draw(screen) and game.end == False:
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        step(personVertice, nextVertice)
        if personVertice == 3:
            graph[3].treasure = False
        if nextVertice == 3:
            return 1
        game.time += 1
        damage_biome(graph, nextVertice, person, weapons)
        sleep(0.2)
        moviment_monster(graph, monsters, weapons)
        print('next')
    return 0

def message_end(game, person, nextVertice):
    if game.time > 120:
        txttela = fontesys.render('Game Over, tempo esgotado', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        return 2
    if person.health == 0 and person.checkpoints_found == -1:
        txttela = fontesys.render('Game Over, muito danano', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        return 2
    if game.statusGame == 2 and game.verticeObjective == 10 and nextVertice == 10:
        txttela = fontesys.render('Parabéns, fase completa!', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        return 2
    return 0


def display_combat(game, monsters, person, weapons):
    global graph
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters, weapons)
    person.draw_explorer_info(fontesys, screen, weapons)
    
    personVertice = depthFirstSearch(graph, graph[0])
    monster = monsters[getMonster(monsters, personVertice)]
    
    if game.combatRound == 3:
        txttela = fontesys.render('Monstro, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))
    elif game.combatRound == 2:
        txttela = fontesys.render('Segundo turno, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))
    elif game.combatRound == 1:
        txttela = fontesys.render('Terceiro turno, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))

    
    if button_scape.draw(screen):
        person.take_damage(monster.attack_points, weapons)
        update_treasure(person, weapons)
            
        game.combatMenu = False
        game.combatRound = 3
        
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        step(personVertice, nextVertice)
        sleep(0.3)
        print('scape')
        
        if nextVertice == 3:
            return 1
    
    if button_combat.draw(screen):
        if game.combatRound == 3:
            person.take_damage(monster.attack_points, weapons)
            update_treasure(person, weapons)
            if person.weapon == None:
                monster.take_damage(person.attack)
            else:
                monster.take_damage(person.attack + weapons[person.weapon].attack_bonus)
            
            
            if monster.health_points == 0:
                monster.health_points = 100
                monster.vertices = searchVerticalEmpty(graph, graph[random.randint(0, len(graph))], weapons)
                game.combatMenu = False
                game.combatRound = 3
            
            game.combatRound = 2
        elif game.combatRound == 2:
            person.take_damage(monster.attack_points, weapons)
            update_treasure(person, weapons)
            if person.weapon == None:
                monster.take_damage(person.attack)
            else:
                monster.take_damage(person.attack + weapons[person.weapon].attack_bonus)
            
            if monster.health_points == 0:
                monster.health_points = 100
                monster.vertices = searchVerticalEmpty(graph, graph[random.randint(0, len(graph))], weapons)
                game.combatMenu = False
                game.combatRound = 3
            
            game.combatRound = 1
        elif game.combatRound == 1:
            person.take_damage(monster.attack_points, weapons)
            update_treasure(person, weapons)
            if person.weapon == None:
                monster.take_damage(person.attack)
            else:
                monster.take_damage(person.attack + weapons[person.weapon].attack_bonus)
            
            if monster.health_points == 0:
                monster.health_points = 100
                monster.vertices = searchVerticalEmpty(graph, graph[random.randint(0, len(graph)) - 1], weapons)
                game.combatMenu = False
                game.combatRound = 3
            
            game.combatMenu = False
            game.combatRound = 3
            nextVertice = nextPosition(personVertice, game.verticeObjective)
            step(personVertice, nextVertice)        
            
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        if nextVertice == 3:
            return 1

        print('combat')
        
    return 0
    
def newVerticeMonster(monsters, weapons):
    newVerticeEmpty = False
    newVertice = 0
    while newVerticeEmpty == False:
        newVertice = searchVerticalEmpty(graph, graph[random.randint(0, len(graph) - 1)], weapons)
        count = 0
        for elementMonster in monsters:
            if elementMonster.vertices == newVertice:
                count += 1
        if count == 0:
            newVerticeEmpty = True
    return newVertice
    
def moviment_monster(graph, monsters, weapons):
    for item in monsters:
        vertice = searchVerticalEmpty(graph, graph[random.randint(0, len(graph) - 1)], weapons)
        monsterVertices = []
        for monster  in monsters:
            if monster.vertices == vertice:
                monsterVertices.append(monster)
        
        if len(monsterVertices) == 0:
            item.vertices = vertice
        elif len(monsterVertices) == 1:
            monsterEnemy = monsterVertices[0]
            if monsterEnemy.attack_points >= item.attack_points:
                item.health_points = 100
                monsterEnemy.take_damage(item.attack_points)
                item.vertices = newVerticeMonster(monsters, weapons)
            else:
                monsterEnemy.health_points = 100
                item.take_damage(monsterEnemy.attack_points)
                monsterEnemy.vertices = newVerticeMonster(monsters, weapons)
        else:
            monsterStrong = monsterVertices[0]
            monsterWeak = monsterVertices[1]
            for elementMonster in monsterVertices:
                if elementMonster.attack_points > monsterStrong.attack_points:
                    monsterStrong = elementMonster
                if elementMonster.attack_points < monsterWeak.attack_points:
                    monsterWeak = elementMonster
            monsterWeak.health_points = 100
            monsterWeak.vertices = newVerticeMonster(monsters, weapons)
            monsterStrong.take_damage(monsterWeak.attack_points)
            for elementMonster in monsterVertices:
                if elementMonster.index != monsterWeak.index != monsterStrong.index:
                    elementMonster.take_damage(monsterStrong.attack_points)
                    if elementMonster.health_points == 0:
                        elementMonster.health_points = 100
                    elementMonster.vertices = newVerticeMonster(monsters, weapons)
                    
def display_weapon(game, monsters, person, weapons):
    global graph
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters, weapons)
    person.draw_explorer_info(fontesys, screen, weapons)
    personVertice = depthFirstSearch(graph, graph[0])
    
    if button_get.draw(screen):
        weapon = getWeapon(weapons, personVertice)
        if person.weapon != None:
            weapons[weapon].vertices = personVertice
        person.weapon = weapon
        weapons[weapon].vertices = -1
        update_treasure(person, weapons)
        game.weaponMenu = False
        print('get weapon')
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        step(personVertice, nextVertice)
        if nextVertice == 3:
            return 1
        game.time += 1
        damage_biome(graph, nextVertice, person, weapons)
        moviment_monster(graph, monsters, weapons)
        sleep(0.3)
        # return 3
    if button_next.draw(screen) and game.end == False:
        game.weaponMenu = False
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        step(personVertice, nextVertice)
        if personVertice == 3:
            graph[3].treasure = False
        if nextVertice == 3:
            return 1
        game.time += 1
        damage_biome(graph, nextVertice, person, weapons)
        sleep(0.2)
        moviment_monster(graph, monsters, weapons)
        print('next')
    return 0

def update_treasure(person, weapons):
    if person.weapon != None:
        if person.treasure_percentage > (person.health-weapons[person.weapon].attack_bonus):
            person.treasure_percentage = (person.health-weapons[person.weapon].attack_bonus)
        if person.treasure_percentage < 0:
            person.treasure_percentage = 0
    else:
        if person.treasure_percentage > person.health:
            person.treasure_percentage = person.health
