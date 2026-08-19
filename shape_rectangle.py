class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Create an object
rectangle = Rectangle(10, 5)

print("Area of rectangle:", rectangle.area())