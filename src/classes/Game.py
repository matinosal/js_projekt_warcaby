from src.classes.Pawns.Pawn import Pawn
from .Player import Player
SIZE = 8
class Game:
    def __init__(self,data):
        self.pawns = []
        self.board = []
        self.playerTurn = 'white'
        self.selectedPawn = None
        self.players = {'white':Player('white'),'black':Player('black')}
        self.forcedMove = False
        self.forcedPawns = []
        for i in range(SIZE):
            self.board.append([])
            self.board[i] = [None] * 10
        for x, y, color in data:
            self.board[x][y] = Pawn(x, y, color)
            self.players[color].incrementPawnAmount()
            #self.player #byc moze kiedys bedzie potrzebne zeby player wiedzial
            #jakie ma pionki
        print(self.board)
    def makeMove(self,x,y,old_x,old_y,take=False):
        self.board[x][y] = self.board[old_x][old_y]
        self.board[old_x][old_y] = None
        self.board[x][y].setNewCoords(x,y)
        if take == True:
            self.players[self.getOppositeColor()].decrementPawnAmount()
            self.checkForNextTake(x,y)

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
    def checkPawnToTake(self,x,y):
        pass #sprawdzenie czy po biciu są pionki do zabrania
    def getOppositeColor(self):
        return 'black' if self.playerTurn == 'white' else 'white'
    def checkForNextTake(self,x,y):
        enemyColor = self.getOppositeColor()
        move_vect  = [(i,j) for i in [-1,1] for j in [-1,1]]
        for vect in move_vect:
            try:
                x_ = x + move_vect[0]
                y_ = y + move_vect[1]
                if self.board[x][y].getColor() == enemyColor:
                    x_ += move_vect[0]
                    y_ += move_vect[1]
            except IndexError as err:
                print('chcialem sie dostac do:',x_,y_)
                pass