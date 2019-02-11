#1. define a class called Apple with four instance variables that represent 4 attributes


class Apple():
    def __init__ (self, c, n, f, v):
        self.color = c
        self.name = n
        self.flavor = f
        self.value = v

apple1 = Apple("red", "Big Red", "bittersweet", "$2.15")
apple2 = Apple("pink", "Pink Lady", "tangy sweet", "$3.05")
apple3 = Apple("green", "Granny Smith", "sour", "$2.05")

print(apple1.color)
print(apple1.name)
print(apple1.flavor)
print(apple1.value)
print("\n")

print(apple2.color)
print(apple2.name)
print(apple2.flavor)
print(apple2.value)
print("\n")


print(apple3.color)
print(apple3.name)
print(apple3.flavor)
print(apple3.value)
print("\n")



import math

class Circle():
    def __init__ (self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi
    
a_circle = Circle(4)
print(a_circle.calculate_area())


class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area1(self):
        return self.height * self.base / 2

a_triangle = Triangle(20,30)
print(a_triangle.calculate_area1())


class Hexagon():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 6

hexagon = Hexagon(3)
print(hexagon.calculate_perimeter())
