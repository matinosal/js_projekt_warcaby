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

    def makeMove(self,x,y,old_x,old_y,take=False):
        self.board[x][y] = self.board[old_x][old_y]
        self.board[old_x][old_y] = None
        self.board[x][y].setNewCoords(x,y)
        self.forcedPawns = []

    def removePawn(self,x,y):
        self.board[x][y] = None
        self.players[self.getOppositeColor()].decrementPawnAmount()
        print("zbito piona na: ",x,y)

    def checkPlayerTurn(self,x,y):
        #tu mozna dac jakis exception ze nie mozna klikac bo wywala blad
        #no idealne miejsce na to
        return self.board[x][y].getColor() == self.playerTurn

    def checkIfSelectedPawn(self):
        return (self.selectedPawn != None)

    def selectPawn(self,x,y):
        self.selectedPawn = None
        if self.forcedMove:
            if self.board[x][y] in self.forcedPawns:
                self.selectedPawn = self.board[x][y]
                return True
            else:
                return False
        self.selectedPawn = self.board[x][y]
        return  True

    def checkIfEmptyField(self,x,y):
        try:
            return self.board[x][y] == None
        except IndexError as err:
            return False

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
    def changeTurn(self):
        self.playerTurn = 'black' if self.playerTurn == 'white' else 'white'
        self.selectedPawn = None
        self.forcedMove = False
        self.forcedPawns = []
        self.scanForMove()

    def checkForNextTake(self,x,y):
        enemyColor = self.getOppositeColor()
        move_vect  = [(i,j) for i in [-1,1] for j in [-1,1]]
        foundForcedMove = False
        try:
            for vect in move_vect:
                x_p = x + vect[0]
                y_p = y + vect[1]
                if not self.checkIfEmptyField(x_p,y_p) and self.board[x_p][y_p].getColor() == enemyColor:
                    x_f = x_p + vect[0]
                    y_f = y_p + vect[1]
                    if x_f in range(0,8) and y_f in range(0,8) and self.checkIfEmptyField(x_f,y_f):
                        self.forcedMove = True
                        self.forcedPawns.append(self.board[x][y])
                        foundForcedMove = True
        except IndexError:
            pass

        return foundForcedMove
    def scanForMove(self):
        for row in self.board:
            for field in row:
                if isinstance(field,Pawn) and field.getColor() == self.playerTurn:
                    x,y = field.getCords()
                    self.checkForNextTake(x,y)
        print('piony do ruchu: ',self.forcedPawns)

