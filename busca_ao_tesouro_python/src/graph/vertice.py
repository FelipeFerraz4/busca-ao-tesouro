import pygame

from src.config.color import *
from src.graph.search import depthFirstSearch

class verticeGraph():
    def __init__(self, id, coordenate, adjacentVertices, person=False, savePoint=False, treasure=False, strangeBiome=0):
        self.id = id
        self.coordinate = (coordenate[0], coordenate[1])
        self.savePoint = savePoint
        self.person = person
        self.adjacentVertices = adjacentVertices
        self.treasure = treasure
        self.item = False
        self.strangeBiome = strangeBiome
    
def draw_vertices(graph, surface):
    for vertice in graph:
        if vertice.person == True:
            pygame.draw.circle(surface, colorPointGreen, vertice.coordinate, 8, 0)
        elif vertice.savePoint == True:
            pygame.draw.circle(surface, colorPointWhite, vertice.coordinate, 8, 0)
        elif vertice.treasure == True:
            pygame.draw.circle(surface, colorPointRed, vertice.coordinate, 8, 0)
        else:
            pygame.draw.circle(surface, colorPointBlue, vertice.coordinate, 8, 0)
            
def draw_edges(graph, surface):
    for vertice in graph:
        for neighboring in vertice.adjacentVertices:
            pygame.draw.line(surface, colorPointBlue, vertice.coordinate, graph[neighboring].coordinate, 2)

def damage_biome(graph, nextVertice, person, weapons):
    biome = graph[nextVertice].strangeBiome
    if biome != -1:
        if biome == 1:
            person.take_damage(10, weapons)
        elif biome == 2:
            person.heal()
        elif biome == 3:
            person.take_damage(15, weapons)
        elif biome == 4:
            person.take_damage(5, weapons)
        elif biome == 5:
            person.take_damage(17, weapons)

    if person.treasure_percentage > person.health:
        person.treasure_percentage = person.health
    