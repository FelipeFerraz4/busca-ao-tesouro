from queue import Empty, Queue
def breadthFirstSearch(graph, vertice, verticeObjective):
    branco = 0
    cinza = 1
    preto = 2
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