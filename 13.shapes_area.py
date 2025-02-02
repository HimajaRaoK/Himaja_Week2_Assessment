'''13. Develop a `Shape` class with a method `area()`. 
Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.'''

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
sq = Square(int(input("Enter the side of the square: ")))
print(f"Area of the square: {sq.area()}")

tri = Triangle(int(input("Enter the base of the triangle: ")), int(input("Enter the height of the triangle: ")))
print(f"Area of the triangle: {tri.area()}")