class Squares():
    square_list = []

    def __init__(self, side):
        self.side = side
        self.square_list.append(side)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

square = Squares(4)
squar2 = Squares(3)
squar3 = Squares(2)

print(Squares.square_list)
print(square)
    
def check_is(obj1, obj2):
    print(obj1 is obj2)

check_is(square, squar2)
