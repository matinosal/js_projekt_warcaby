import init_data as data
from Game import Game
from tkinter import *

game = Game(data.board_setup)
print(game.pawns)
