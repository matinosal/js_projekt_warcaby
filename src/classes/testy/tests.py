import unittest
import src.classes.GameUI
import src.classes.Game
import src.classes.init_data
from src.classes.Pawns.Queen import Queen
class MyTestCase(unittest.TestCase):
    def test_1(self):
        ui = src.classes.GameUI.GameUI(True)
        white_pawn = ui.game.board[2][4] #zapisanie referencji do piona, którym ruszamy(biały)
        ui.clickHandler(2,4) #wybór piona białego
        ui.clickHandler(3, 3) #ruch piona na pole 3,3

        black_pawn = ui.game.board[5][5] #zapisanie referencji do piona, którym ruszamy(czarny)
        ui.clickHandler(5, 5)  # wybór piona na polu 5 5
        ui.clickHandler(4, 6)  # ruch piona na pole 6,4

        self.assertEqual(white_pawn, ui.game.board[3][3]) #sprawdzenie czy wykonał się 1 ruch bialego
        self.assertEqual(black_pawn, ui.game.board[4][6]) #sprawdzenie czy wykonał się 1 ruch czarnego

        white_pawn = ui.game.board[2][2]  # zapisanie referencji do piona, którym ruszamy(biały)
        ui.clickHandler(2, 2)  # wybór piona białego
        ui.clickHandler(3, 1)  # ruch piona na pole 3,3

        ui.clickHandler(4, 6)  # wybór piona na polu 5 5
        ui.clickHandler(3, 7)  # ruch piona na pole 6,4

        self.assertEqual(white_pawn, ui.game.board[3][1]) #sprawdzenie czy wykonał się 2 ruch bialego
        self.assertEqual(black_pawn, ui.game.board[3][7]) #sprawdzenie czy wykonał się 2 ruch czarnego
        del ui

    def test_2(self):
        ui = src.classes.GameUI.GameUI(True)
        white_pawn = ui.game.board[2][4]  # zapisanie referencji do piona, którym ruszamy(biały)
        ui.clickHandler(2, 4)  # wybór piona białego
        ui.clickHandler(3, 4)  # ruch piona na pole 3,3

        self.assertEqual(white_pawn, ui.game.board[2][4])  # sprawdzenie czy nie wykonał się ruch

        del ui

    def test_3(self):
        ui = src.classes.GameUI.GameUI(True)
        test_board = [
            (1, 1, "black"),
            (1, 3, "black"),
            (2, 2, "white")
        ]
        game = src.classes.Game.Game(test_board)
        ui.game = game
        white_pawn = ui.game.board[2][2]  # zapisanie referencji do piona, którym ruszamy(biały)
        ui.clickHandler(2, 2)  # wybór piona białego
        ui.clickHandler(0, 0)  # bicie piona na 1,1

        self.assertEqual(white_pawn, ui.game.board[0][0])
        self.assertEqual(None,ui.game.board[1][1])
        del ui

    def test_4(self):
        ui = src.classes.GameUI.GameUI(True)
        test_board = [
            (7, 7, "black"),
            (1, 1, "black"),
            (3, 3, "black"),
            (4, 4, "white")
        ]
        game = src.classes.Game.Game(test_board)
        ui.game = game
        white_pawn = ui.game.board[4][4]  # zapisanie referencji do piona, którym ruszamy(biały)
        ui.clickHandler(4, 4)  # wybór piona białego
        ui.clickHandler(2, 2)  # bicie piona na 3,3
        ui.clickHandler(2, 2)  # wybór piona białego
        ui.clickHandler(0, 0)  # bicie piona na 1,1
        self.assertEqual(white_pawn, ui.game.board[0][0])
        self.assertEqual(None, ui.game.board[1][1])
        self.assertEqual(None, ui.game.board[3][3])

        del ui

    def test_5(self):
        ui = src.classes.GameUI.GameUI(True)
        test_board = [
            (1, 1, "black"),
            (3, 3, "black"),
            (6, 6, "white")
        ]
        game = src.classes.Game.Game(test_board)
        ui.game = game
        ui.clickHandler(6, 6)  # wybór piona białego
        ui.clickHandler(7, 7)  # ruch pionem na pole 7,7
        self.assertEqual(True, isinstance(ui.game.board[7][7],Queen)) #sprawdzam czy typ pionka sie zmienił z Pawn na Queen

        del ui
    def test_6(self):
        ui = src.classes.GameUI.GameUI(True)
        test_board = [
            (1, 1, "black"),
            (3, 3, "black"),
            (6, 6, "white")
        ]
        game = src.classes.Game.Game(test_board)
        ui.game = game
        ui.clickHandler(6, 6)  # wybór piona białego
        ui.clickHandler(7, 7)  # ruch pionem na pole 7,7

        ui.clickHandler(1, 1)  # wybór piona czarnego
        ui.clickHandler(0, 0)  # ruch pionem na pole 0,0
        white_queen = ui.game.board[7][7]
        ui.clickHandler(7, 7)  # wybór białej królowej
        ui.clickHandler(2, 2)
        self.assertEqual(white_queen, ui.game.board[2][2])

        del ui
    def test_7(self):
        ui = src.classes.GameUI.GameUI(True)
        test_board = [
            (5, 5, "black"),
            (6, 6, "white")
        ]
        game = src.classes.Game.Game(test_board)
        ui.game = game
        ui.game.changeTurn() #zmieniam turę dla czarnego gracza
        self.assertEqual('', ui.game.winner)
        ui.clickHandler(5, 5)  # wybór piona czarnego
        ui.clickHandler(7, 7)  # ruch pionem na pole 7,7 bicie piona na 6,6
        self.assertEqual('czarny',ui.lastGameWinner)

        del ui
    def test_8(self):
        ui = src.classes.GameUI.GameUI(True)
        test_board = [
            (5, 5, "black"),
            (6, 6, "white")
        ]
        game = src.classes.Game.Game(test_board)
        ui.game = game
        ui.game.changeTurn() #zmieniam turę dla czarnego gracza
        ui.clickHandler(5, 5)  # wybór piona czarnego
        ui.clickHandler(7, 7)  # ruch pionem na pole 7,7 bicie piona na 6,6
        self.assertEqual(ui.game.players['black'].pawnCount,12)
        self.assertEqual(ui.game.players['black'].pawnCount, 12)
        del ui
if __name__ == '__main__':
    unittest.main()
