class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


rect = Rectangle(4, 5)
print("Square: ", rect.square())
print("Perimeter: ", rect.perimeter())
