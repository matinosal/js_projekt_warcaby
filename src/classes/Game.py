from src.classes.Pawns.Pawn import Pawn
from src.classes.Pawns.Queen import Queen
from src.classes.Pawns.PawnObj import PawnObj
from .Player import Player

SIZE = 8
class Game:
    def __init__(self,data):
        '''Konstruktor, przyjmujący jako argument ułożenie pionów na planszy'''
        self.pawns = []
        self.board = []
        self.playerTurn = 'white'
        self.winner = ''
        self.selectedPawn = None
        self.players = {'white':Player('white'),'black':Player('black')}
        self.forcedMove = False
        self.forcedPawns = []
        self.possibleMove = True
        for i in range(SIZE):
            self.board.append([])
            self.board[i] = [None] * 10
        for x, y, color in data:
            self.board[x][y] = Pawn(x, y, color)
            self.players[color].incrementPawnAmount()
            #self.player #byc moze kiedys bedzie potrzebne zeby player wiedzial
            #jakie ma pionki

    def makeMove(self,x,y,old_x,old_y):
        '''Przenosi referencje do obiektu pionka do innego miejsca w macierzy'''
        self.board[x][y] = self.board[old_x][old_y]
        self.board[old_x][old_y] = None
        self.board[x][y].setNewCoords(x,y)
        self.forcedPawns = []
        self.checkPromotion(x,y)

    def removePawn(self,x,y):
        '''Usuwa referencje do obiektu pionka z macierzy board i zmniejsza ilosc pionkow danego gracza'''
        self.board[x][y] = None
        self.players[self.getOppositeColor()].decrementPawnAmount()

    def checkPlayerTurn(self,x,y):
        '''sprawdza czy kolor bierki jest taki sam jak gracza'''
        return self.board[x][y].getColor() == self.playerTurn

    def checkIfSelectedPawn(self):
        '''zwraca informacje o tym czy jakis pionek zostal wybrany'''
        return (self.selectedPawn != None)

    def selectPawn(self,x,y):
        '''wybiera danego piona'''
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
        '''sprawdza czy podane pole jest puste'''
        if x in range(0,8) and y in range(0,8):
            return self.board[x][y] == None
        return True

    def getClickedFieldType(self,x,y):
        return 'pawn' if self.board[x][y] != None else 'square'
    def getSelectedType(self):
        return 'pawn' if  isinstance(self.selectedPawn,Pawn) else 'queen'
    def getSelectedPawnInfo(self):
        return self.selectedPawn.getPawnInfo()
    def getOppositeColor(self):
        return 'black' if self.playerTurn == 'white' else 'white'
    def changeTurn(self):
        '''zmiana tury gracza oraz wywolanie skanowania w poszukiwaniu ruchu/bicia'''
        self.playerTurn = 'black' if self.playerTurn == 'white' else 'white'
        self.selectedPawn = None
        self.forcedMove = False
        self.scanForMove()
        if self.players[self.playerTurn].pawnCount == 0 or not self.possibleMove:
            self.winner = 'biały' if self.getOppositeColor() == 'white' else 'czarny'


    def checkForNextTake(self,x,y):
        '''sprawdzenie czy jest bicie daną bierką, sprawdzenie różni się od typu bierki'''
        enemyColor = self.getOppositeColor()
        move_vect  = [(i,j) for i in [-1,1] for j in [-1,1]]
        foundForcedMove = False
        if isinstance(self.board[x][y],Queen):
            try:
                for vect in move_vect:
                    x_ = x
                    y_ = y
                    for mull in range(1,8):
                        x_ += vect[0]
                        y_ += vect[1]
                        if not x_ in range(1,7) or not y_ in range(1,7):
                            break;
                        if isinstance(self.board[x_][y_],PawnObj) and self.board[x_][y_].getColor() == self.playerTurn:
                            break
                        if isinstance(self.board[x_][y_],PawnObj) and self.checkIfEmptyField(x_+vect[0],y_+vect[1]):
                            self.forcedMove = True
                            self.forcedPawns.append(self.board[x][y])
                            self.possibleMove = True
                            foundForcedMove = True
            except IndexError:
                pass
        try:
            for vect in move_vect:
                x_p = x + vect[0]
                y_p = y + vect[1]
                if not self.checkIfEmptyField(x_p,y_p) and self.board[x_p][y_p].getColor() == enemyColor:
                    x_f = x_p + vect[0]
                    y_f = y_p + vect[1]
                    if self.XYInRange(x_f,y_f) and self.checkIfEmptyField(x_f,y_f):
                        self.forcedMove = True
                        self.forcedPawns.append(self.board[x][y])
                        self.possibleMove = True
                        foundForcedMove = True

        except IndexError:
            pass
        return foundForcedMove
    def scanForMove(self):
        '''skanuje całą planszę w poszukiwaniu ruchów gracza '''
        self.possibleMove = False
        for row in self.board:
            for field in row:
                if isinstance(field,PawnObj) and field.getColor() == self.playerTurn:
                    x,y = field.getCords()
                    self.checkForNextTake(x,y)
                    if self.possibleMove == False:
                        self.checkForPossibleMove(x,y,field.getColor())


    def checkPromotion(self,x,y):
        '''sprawdza czy dany pion ma zostac wypromowany'''
        if (self.playerTurn == 'white' and x == 7) or (self.playerTurn=='black' and x == 0):
            self.promotePawn(x,y)
    def promotePawn(self,x,y):
        '''promocja piona na damkę'''
        self.board[x][y] = Queen(x,y,self.playerTurn)
    def XYInRange(self,x,y):
        if x in range(0,8) and y in range(0,8):
            return True
        return False
    def checkForPossibleMove(self,x,y,color):
        '''Sprawdza czy gracz moze wykonac ruch daną bierka, jest to wymagane zeby mozna bylo doprowadzic do remisu z powodu braku ruchu'''
        if isinstance(self.board[x][y],Pawn):
            y_ = y+1 if color == 'white' else y-1
            if self.checkIfEmptyField(x+1,y_) or self.checkIfEmptyField(x-1,y_):
                self.possibleMove = True
        else:
            move_vect = [(i, j) for i in [-1, 1] for j in [-1, 1]]
            for vect in move_vect:
                new_x = x
                new_y = y
                for step in range(0,7):
                    new_x,new_y = new_x+vect[0],new_y+vect[1]
                    if self.checkIfEmptyField(new_x,new_y) and self.XYInRange(x,y):
                        self.possibleMove = True
                    elif isinstance(self.board[x+vect[0]][y+vect[1]],PawnObj):
                        break
