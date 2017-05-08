class Shape():
    @staticmethod
    def printType():
        print("static method")
    def draw(self):
        print("draw")
    def area(self):
        print("area")

class rectangle(Shape):
    def __init__(self):
        self.width = 23
        self.length =34


class triangle(Shape):
    def __init__(self):
        self.a = 2
        self.b = 3
        self.c = 4
    def draw(self):
       print("draw again2")
    def area(self):
       print("area again2")

s = Shape()
s.printType()
t = triangle()
r = rectangle()
s.area()
s.draw()
r.draw()
t.draw()



