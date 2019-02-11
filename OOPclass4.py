class SquareTwo():
    square_list = []
    
    def __init__(self, s2):
        self.s2 = s2
        self.square_list.append(self)
        
    def calculate_perim(self):
        return self.s2 * 4

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s2, self.s2, self.s2, self.s2)
    
sq_four = SquareTwo(29)
print(sq_four)


class Square():

    sqrs = []
    
    def __init__(self, s):
        self.s = s
        self.sqrs.append(self)

    def calculate_perim(self):
        return self.s * 4

    def __repr__(self):
            return "{} by {}" .format(self.s, self.s)
            
sq_one = Square(4)
print(Square.sqrs)
sq_two = Square(9)
print(Square.sqrs)
sq_three = Square(12)
print(Square.sqrs)
