class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Created!")

    def calc_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Created!")

    def calc_area(self):
        return self.width * self.height

    def change_size(self, change):
        self.width = self.width + change
        self.height = self.height + change

rect = Rectangle(4, 5)
squa = Square(4, 4)
print(rect.calc_area())
print(squa.calc_area())
squa.change_size(-2)
print(squa.calc_area())
rect.what_am_i()
squa.what_am_i()

class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider
        print("Created!")

class Rider():
    def __init__(self, name):
        self.name = name

chuck = Rider("Chuck")
dave = Horse("Dave", chuck)
print(dave.rider.name)
