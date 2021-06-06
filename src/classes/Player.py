class Player:
    def __init__(self,color_):
        self.color = color_
        self.pawnCount = 0
        self.pawns = []
    def incrementPawnAmount(self):
        self.pawnCount += 1
    def decrementPawnAmount(self):
        self.pawnCount -= 1
    def __str__(self):
        return "jestem {0} pionki: {1}".format(self.color,self.pawnCount)
    def __repr__(self):
        return "jestem {0} pionki: {1}".format(self.color,self.pawnCount)