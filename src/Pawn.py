class Pawn:
    def __init__(self,x_,y_,color):
        self.x = x_
        self.y = y_
        self.color = color

    def __str__(self):
        return 'Jestem pion x:{0} y:{1} kolor:{2}'.format(self.x,self.y,self.color)

    def __repr__(self):
        return 'Jestem pion x:{0} y:{1} kolor:{2}'.format(self.x, self.y, self.color)