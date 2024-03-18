class verticeGraph():
    def __init__(self, id, coordenate, adjacentVertices, person=False, savePoint=False):
        self.id = id
        self.coordinate = (coordenate[0], coordenate[1])
        self.savePoint = savePoint
        self.person = person
        self.adjacentVertices = adjacentVertices
        self.treasure = 0
        self.item = False
        self.strangeBiome = False
    