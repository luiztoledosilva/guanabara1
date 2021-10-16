class Point:

    def __init__(self, x,y):
        self.x=x
        self.y=y

    def setx(self,x):
        self.x=x

    def sety(self,y):
        self.y=y

    def get(self):
        return self.x, self.y

    def move(self,offsetx,offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '({0},{1})'.format(str(self.x), str(self.y))


#p=Point()
##q=Point(3,4)
#q.move(3,-5)
