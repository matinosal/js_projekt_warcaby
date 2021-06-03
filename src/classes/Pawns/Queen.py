from src.classes.Pawns.PawnObj import PawnObj
class Queen(PawnObj):
    def __str__(self):
        return 'Jestem damka x:{0} y:{1} kolor:{2}'.format(self.x,self.y,self.color)
