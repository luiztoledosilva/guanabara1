class Point2():
    def __init__(self, x=0, y=0):

        self.x = x

        self.y = y

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    def __add__(self, other):
        if type(other) == Point2:
            return Point2(self.x + other.x, self.y +
                         other.y)

        else:
            return Point2(self.x + other, self.y + other)