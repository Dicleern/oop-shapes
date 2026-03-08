# pylint: disable=too-few-public-methods missing-module-docstring
pass  # YOUR CODE HERE
class Shape:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def say_name(self):
        return f"My name is {self.name}."

if __name__ == "__main__":
    test_shape = Shape("red", "Shape")
    print(test_shape.say_name())

class Rectangle(Shape):
    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        return f"My name is {self.name} and I am a circle."

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius
if __name__ == "__main__":
    rect = Rectangle("blue", "Bob", 4, 5)
    print(rect.say_name())
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    circ = Circle("green", "Dora", 3)
    print(circ.say_name())
    print(f"Area: {circ.area()}")
    print(f"Perimeter: {circ.perimeter()}")
