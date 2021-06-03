import tkinter as tk
from .Game import Game
from .init_data import *
from functools import partial
from src.classes.Pawns.Pawn import Pawn
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
            text='Tura gracza 2',
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
            if self.game.checkIfEmptyField(x,y) and self.game.getSelectedType(x,y) == 'pawn': #ruch pionka
                if not self.game.moveAllowed(x,y):
                    self.displayWarning()
                    return
                pawn_x,pawn_y,color = self.game.getSelectedPawnInfo()
                move_vect_x = (x - pawn_x) *(-1 if self.game.selectedPawn.getColor() == 'black' else 1)
                move_vect_y = abs(y - pawn_y)
                if move_vect_y == 1 and move_vect_x == 1 and not self.game.forcedMove: #ruch o jedno pole
                    self.displayMove(x, y, pawn_x, pawn_y)
                    self.game.makeMove(x,y,pawn_x,pawn_y)
                    self.game.changeTurn()
                if abs(move_vect_x) == 2 and move_vect_y == 2:#ruch o dwa pola(bicie)
                    mid_point_x = (x+pawn_x)//2
                    mid_point_y = (y + pawn_y) // 2
                    mid_pawn = self.game.board[mid_point_x][mid_point_y]
                    if not (isinstance(mid_pawn,Pawn) and  mid_pawn.getColor() != color):
                        self.displayWarning()
                        return
                    self.displayMove(x, y, pawn_x, pawn_y)
                    self.game.makeMove(x, y, pawn_x, pawn_y,True)
                    self.hidePawn(mid_point_x,mid_point_y)
                    self.game.removePawn(mid_point_x, mid_point_y)
                    if not self.game.checkForNextTake(x,y):
                        self.game.changeTurn()
                return
            if not self.game.checkPlayerTurn(x,y):
                self.displayWarning()
                return
            if self.game.getClickedFieldType(x,y) == 'pawn': # zmiana pionka
                old_x,old_y = self.game.selectedPawn.getCords()
                self.buttons[old_x][old_y].configure(text='B' if board[x][y].getColor() == 'white' else 'C')
                if self.game.selectPawn(x, y):
                    self.buttons[x][y].configure(text='[B]' if board[x][y].getColor() == 'white' else '[C]')
                else:
                    self.displayWarning()
        else:
            if self.game.checkIfEmptyField(x,y) or not self.game.checkPlayerTurn(x,y):
                self.displayWarning()
                return
            if self.game.selectPawn(x, y):
                self.buttons[x][y].configure(text='[B]' if board[x][y].getColor() == 'white' else '[C]')
            else:
                self.displayWarning()

    def displayMove(self,x,y,new_x,new_y):
        self.buttons[x][y].configure(text='B' if self.game.selectedPawn.getColor() == 'white' else 'C')
        self.buttons[new_x][new_y].configure(text='')
    def displayWarning(self):
        self.warning_info.configure(text='Ruch niedozwolony')
    def hidePawn(self,x,y):
        self.buttons[x][y].configure(text='')