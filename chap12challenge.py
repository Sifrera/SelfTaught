class Apple():
    def __init__(self, c, w, s, r):
        self.color = c
        self.weight = w
        self.shine = s
        self.ripe = r
        print("Created!")

apple = Apple("red", 10, "shiny", "ripe")

import math

class Circle():
    def __init__(self, r):
        self.radius = r


    def calculate_area(self):
        return self.radius ** 2 * math.pi

circle = Circle(5)
print(circle.calculate_area())

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
        print("Created!")

    def calc_area(self):
        return self.base * self.height / 2

trian = Triangle(2, 4)
print(trian.calc_area())

class RegHexagon():
    def __init__(self, side):
        self.side = side
        print("Created!")

    def calc_perimeter(self):
        return self.side * 6

flexo = RegHexagon(2)
print(flexo.calc_perimeter())
