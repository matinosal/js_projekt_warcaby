import tkinter as tk
from .Game import Game
from .init_data import *
from functools import partial
from src.classes.Pawns.PawnObj import PawnObj
from src.classes.Pawns.Queen import Queen
SIZE = 8
class GameUI:
    def __init__(self):
        self.game = Game(board_setup)
        self.buttons = []
        self.createWindow()

    def createWindow(self):
        color = "#000000"
        secondary_c = '#ffffff'
        window = tk.Tk()
        self.makeTextLabels(window)
        button = tk.Button(
            master=window,
            text="reset",
            padx=10,
            pady=10,
            command=self.reset
        )
        button.pack(side='top')
        pixelVirtual = tk.PhotoImage(width=1, height=1)
        main_frame = tk.Frame(master=window)
        main_frame.pack(side='top')


        for i in range(SIZE):
            self.buttons.append([])
            for j in range(SIZE):
                button = tk.Button(
                    master=main_frame,
                    relief=tk.RAISED,
                    image=pixelVirtual,
                    borderwidth=1,
                    width=100,
                    height=100,
                    fg=color,
                    bg=secondary_c,
                    text="",
                    compound="c",
                    command=partial(self.clickHandler, (SIZE - 1 - i), j, self.game.board)
                )
                self.buttons[i].append(button)
                button.grid(row=i, column=j)
                color = '#000000' if color == '#ffffff' else '#ffffff'
                secondary_c = '#ffffff' if color == '#000000' else '#000000'
            color = '#000000' if color == '#ffffff' else '#ffffff'
            secondary_c = '#ffffff' if color == '#000000' else '#000000'
        self.buttons.reverse()
        self.setPawns(self.game.board)
        window.mainloop()

    def makeTextLabels(self,window):
        self.turn_info = tk.Label(
            text='Tura gracza 1 (biały)',
            master=window,
            pady=10,
            padx=10,
        )
        self.turn_info.pack(side='top')

        self.warning_info = tk.Label(
            text='',
            master=window,
            pady=10,
            padx=10
        )
        self.warning_info.pack(side='top')

    def setPawns(self,board):
        for row in board:
            for square in row:
                if square != None:
                    x,y,color = square.getPawnInfo()
                    self.buttons[x][y].configure(text= 'B' if 'white'==color else 'C')
    def clickHandler(self,x,y,board):
        if self.game.checkIfSelectedPawn():
            if self.game.checkIfEmptyField(x,y) and self.game.getSelectedType() == 'pawn': #ruch pionka
                pawn_x,pawn_y,color = self.game.getSelectedPawnInfo()
                move_vect_x = (x - pawn_x) *(-1 if self.game.selectedPawn.getColor() == 'black' else 1)
                move_vect_y = abs(y - pawn_y)
                if move_vect_y == 1 and move_vect_x == 1 and not self.game.forcedMove: #ruch o jedno pole
                    self.game.makeMove(x,y,pawn_x,pawn_y)
                    self.displayMove(x, y, pawn_x, pawn_y)
                    self.newTurn()
                if abs(move_vect_x) == 2 and move_vect_y == 2:#ruch o dwa pola(bicie)
                    mid_point_x = (x+pawn_x)//2
                    mid_point_y = (y + pawn_y) // 2
                    mid_pawn = self.game.board[mid_point_x][mid_point_y]
                    if not (isinstance(mid_pawn,PawnObj) and  mid_pawn.getColor() != color):
                        self.displayWarning()
                        return
                    self.game.makeMove(x, y, pawn_x, pawn_y)
                    self.displayMove(x, y, pawn_x, pawn_y)
                    self.hidePawn(mid_point_x,mid_point_y)
                    self.game.removePawn(mid_point_x, mid_point_y)
                    if not self.game.checkForNextTake(x,y):
                        self.newTurn()
                return
            if self.game.checkIfEmptyField(x,y) and self.game.getSelectedType() == 'queen':
                queen_x,queen_y,color = self.game.getSelectedPawnInfo()
                vect = [queen_x-x,queen_y-y]
                if (abs(vect[0])-abs(vect[1])) == 0:
                    vect = [vect[0]//abs(vect[0]),vect[1]//abs(vect[1])]
                    if self.game.forcedMove:
                        skippedPawn = 0
                        for step in range(1,abs(queen_x-x)):
                            print('znalazlem piona na polu:', queen_x - step * vect[0], queen_y - step * vect[1])
                            if isinstance(self.game.board[queen_x - step*vect[0]][queen_y - step*vect[1]],PawnObj):
                                skipped_x , skipped_y = queen_x - step*vect[0],queen_y - step*vect[1]
                                skippedPawn +=1
                        if skippedPawn == 1:
                            self.game.makeMove(x, y, queen_x, queen_y)
                            self.displayMove(x, y, queen_x, queen_y)
                            self.hidePawn(skipped_x ,skipped_y)
                            self.game.removePawn(skipped_x ,skipped_y)
                            if not self.game.checkForNextTake(x, y):
                                self.newTurn()
                    else:
                        for step in range(1,abs(queen_x-x)):
                            if isinstance(self.game.board[queen_x - step*vect[0]][queen_y - step*vect[1]],PawnObj):
                                return
                        self.game.makeMove(x, y, queen_x, queen_y)
                        self.displayMove(x, y, queen_x, queen_y)
                        self.newTurn()
                return

            if not self.game.checkPlayerTurn(x,y):
                self.displayWarning()
                return
            if self.game.getClickedFieldType(x,y) == 'pawn': # zmiana pionka
                old_x,old_y = self.game.selectedPawn.getCords()
                self.changeFieldText(old_x,old_y)
                if self.game.selectPawn(x, y):
                    self.changeFieldText(x,y,True)
                else:
                    self.displayWarning()
        else:
            if self.game.checkIfEmptyField(x,y) or not self.game.checkPlayerTurn(x,y):
                self.displayWarning()
                return
            if self.game.selectPawn(x, y):
                self.changeFieldText(x,y,True)
            else:
                self.displayWarning()

    def displayMove(self,x,y,new_x,new_y):
        self.changeFieldText(x,y)
        self.buttons[new_x][new_y].configure(text='')

    def displayWarning(self):
        self.warning_info.configure(text='Ruch niedozwolony')
    def hidePawn(self,x,y):
        self.buttons[x][y].configure(text='')
    def changeFieldText(self,x,y,select=False):
        text_ ='B' if self.game.selectedPawn.getColor() == 'white' else 'C'
        if isinstance(self.game.board[x][y], Queen):
            text_ = text_ + "d"
        if select:
            text_ = "["+text_+"]"
        self.buttons[x][y].configure(text=text_)
    def newTurn(self):
        self.game.changeTurn()
        self.changeLabelText()
    def changeLabelText(self):
        if self.game.winner != '':
            text_ = 'Wygrał gracz: ' + self.game.winner
            winnerInfo = tk.Tk()
            winnerLabel = tk.Label(
                text=text_,
                master=winnerInfo,
                pady=10,
                padx=10,
            )
            winnerLabel.pack(side='top')
        else:
            text_ = 'Tura gracza nr 1 (biały)' if self.game.playerTurn == 'white' else 'Tura gracza nr 2 (czarny)'
        self.turn_info.configure(text=text_)
    def reset(self):
        del self.game
        self.game = Game(board_setup)
        for i in range(len(self.game.board)):
            for j in range(len(self.game.board)):
                if isinstance(self.game.board[i][j],PawnObj):
                    color = self.game.board[i][j].getColor()
                    self.buttons[i][j].configure(text= 'B' if 'white'==color else 'C')
                else:
                    self.buttons[i][j].configure(text='')
        self.turn_info.configure(text='Tura gracza: 1 (biały)')