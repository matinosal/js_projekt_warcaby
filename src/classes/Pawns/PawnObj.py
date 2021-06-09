class PawnObj:
    def __init__(self,x_,y_,color):
        self.x = x_
        self.y = y_
        self.color = color

    def getPawnInfo(self):
        '''Zwraca informacje na temat bierki'''
        return self.x,self.y,self.color
    def getColor(self):
        '''zwraca kolor danej bierki'''
        return self.color
    def getCords(self):
        return self.x,self.y
    def setNewCoords(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        '''służy do wyświetlania w konsoli informacji o obiekcie'''
        return '{0}'.format(self.color)
    def __str__(self):
        '''służy do wyświetlania w konsoli informacji o obiekcie'''
        return '{0}'.format(self.color)