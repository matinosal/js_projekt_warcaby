from Pawn import Pawn
SIZE = 8
class Game:
    def __init__(self,data):
        self.pawns = []
        self.board = []
        self.playerTurn = 'white'
        self.selectedPawn = None
        for i in range(SIZE):
            self.board.append([])
            self.board[i] = [None] * 10
        for x, y, color in data:
            self.board[x][y] = Pawn(x, y, color)
        print(self.board)
    def makeMove(self,x,y,old_x,old_y):
        self.board[x][y] = self.board[old_x][old_y]
        self.board[old_x][old_y] = None
        self.board[x][y].setNewCoords(x,y)
        print("stary:",self.board[old_x][old_y])
        print("nowy:",self.board[x][y])
        self.playerTurn = 'black' if self.playerTurn == 'white' else 'white'
        self.selectedPawn = None
    def removePawn(self,x,y):
        self.board[x][y] = None
    def checkPlayerTurn(self,x,y):
        #tu mozna dac jakis exception ze nie mozna klikac bo wywala blad
        #no idealne miejsce na to
        return self.board[x][y].getColor() == self.playerTurn

    def checkIfSelectedPawn(self):
        return (self.selectedPawn != None)

    def selectPawn(self,x,y):
        self.selectedPawn = self.board[x][y]

    def checkIfEmptyField(self,x,y):
        return self.board[x][y] == None

    def getClickedFieldType(self,x,y):
        return 'pawn' if self.board[x][y] != None else 'square'
    def getSelectedType(self,x,y):
        return 'pawn' if  isinstance(self.selectedPawn,Pawn) else 'queen'
    def moveAllowed(self,x,y):#do napisania jak będzie robione bicie
        return True
    def getSelectedPawnInfo(self):
        return self.selectedPawn.getPawnInfo()