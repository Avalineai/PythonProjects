class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square():
    def __init__(self, s1):
        self.s1= s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 50)
a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())


class SquareTwo():
    def __init__(self, s2):
        self.s2 = s2

    def calculate_perim(self):
        return self.s2 * 4

    def change_size(self, new_size):
        self.s2 += new_size

b_square = SquareTwo(100)
print(b_square.s2)

b_square.change_size(200)
print(b_square.s2)
