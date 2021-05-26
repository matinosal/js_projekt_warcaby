from Pawn import Pawn
class Game:
    def __init__(self,data):
        self.pawns = []
        for x, y, color in data:
            self.pawns.append(Pawn(x, y, color))