class verticeGraph():
    def __init__(self, id, coordenate, adjacentVertices):
        self.id = id
        self.coordinate = (coordenate[0], coordenate[1])
        self.savePoint = False
        self.person = False
        self.adjacentVertices = adjacentVertices
        self.treasure = 0
        self.item = False
        self.strangeBiome = False
    