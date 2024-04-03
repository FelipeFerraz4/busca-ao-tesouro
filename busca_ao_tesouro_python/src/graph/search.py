from queue import Empty, Queue
# from main import graph
from src.character.weapon import *
branco = 0
cinza = 1
preto = 2

# achar o melhor visinho para atigir o objetivo mais rápido
def breadthFirstSearch(graph, vertice, verticeObjective):
    color = []
    # distance = []
    father = []
    queue = []
    # teste = []
    
    for item in graph:
        # teste.append(item.id)
        color.append(branco)
        # distance.append(1000) #infinito
        father.append(-1)
        
    color[vertice.id] = cinza
    # distance[vertice.id] = 0
    
    queue.append(vertice)

    while len(queue) !=  0:
        verticeW = queue.pop(0)
        for verticeV in verticeW.adjacentVertices:
            if color[verticeV] == branco:
                color[verticeV] = cinza
                # distance[verticeV] = distance[verticeW.id] + 1
                father[verticeV] = verticeW.id
                queue.append(graph[verticeV])
        color[verticeW.id] = preto

    # print(distance)
    # print(teste)
    # print(father)
    
    verticeU = verticeObjective.id
    verticeAnterio = verticeU
    while verticeU != vertice.id:
        verticeAnterio = verticeU
        verticeU = father[verticeU]
    # print(verticeU)
    # print(verticeAnterio)
    return verticeAnterio


def visit(graph, vertice, color):
    color[vertice.id] = cinza
    status = -1
    
    for verticeV in vertice.adjacentVertices:
        if graph[verticeV].person == True:
            return graph[verticeV].id
        if color[graph[verticeV].id] == branco:
            status = visit(graph, graph[verticeV], color)
        if status != -1:
            return status
    
    color[vertice.id] = preto
    return status

# achar o persongem no grafo
def depthFirstSearch(graph, vertice):
    color = []
    
    for item in graph:
        color.append(branco)
    return visit(graph, vertice, color)

#acha um vertice considerado vazio
def searchVerticalEmpty(graph, vertice, weapons):
    color = []
    queue = []
    
    for item in graph:
        color.append(branco)
        
    color[vertice.id] = cinza
    
    queue.append(vertice)

    while len(queue) !=  0:
        verticeW = queue.pop(0)
        for verticeV in verticeW.adjacentVertices:
            if graph[verticeV].treasure == False and graph[verticeV].strangeBiome == -1 and graph[verticeV].savePoint == False and isWeapon(weapons, verticeV) == False:
                return verticeV
            if color[verticeV] == branco:
                color[verticeV] = cinza
                queue.append(graph[verticeV])
        color[verticeW.id] = preto
    return 10