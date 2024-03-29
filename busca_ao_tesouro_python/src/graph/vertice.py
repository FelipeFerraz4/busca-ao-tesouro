import pygame

from src.config.color import *

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