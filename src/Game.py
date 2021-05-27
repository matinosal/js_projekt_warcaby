from Pawn import Pawn
SIZE = 8
class Game:
    def __init__(self,data):
        self.pawns = []
        self.board = []
        self.playerTurn = 'white'
        for i in range(SIZE):
            self.board.append([])
            self.board[i] = [None] * 10
        for x, y, color in data:
            self.board[x][y] = Pawn(x, y, color)
        print(self.board)

    def checkPlayerTurn(self,x,y):
        return self.board[x][y].getColor() == self.playerTurn