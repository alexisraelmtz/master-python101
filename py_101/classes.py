class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point(90, 20)
# point1.y = 90
# point1.x = 20
print(point1.y)
point1.draw()


point2 = Point(1, 2)
# point2.x = 1
print(point2.y)
