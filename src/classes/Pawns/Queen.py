class Queen:
    def __init__(self,x_,y_,color):
        self.x = x_
        self.y = y_
        self.color = color

    def getPawnInfo(self):
        return self.x,self.y,self.color
    def getColor(self):
        return self.color
    def getCords(self):
        return self.x,self.y
    def setNewCoords(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Jestem damka x:{0} y:{1} kolor:{2}'.format(self.x,self.y,self.color)

    def __repr__(self):
        return '{0}'.format(self.color)