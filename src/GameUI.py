import tkinter as tk
from Game import Game
from init_data import *
from functools import partial
from Pawn import Pawn

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
    def clickHandler(self,i,j,board):
        if not self.game.checkPlayerTurn(i,j):
            self.displayWarning()
            return
        self.buttons[i][j].configure(text='klikniety')
    def displayWarning(self):
        self.warning_info.configure(text='Ruch niedozwolony')