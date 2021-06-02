class Player:
    def __init__(self,color_):
        self.color = color_
        self.pawnCount = 0
        self.pawns = []
    def incrementPawnAmount(self):
        self.pawnCount += 1
    def decrementPawnAmount(self):
        self.pawnCount -= 1