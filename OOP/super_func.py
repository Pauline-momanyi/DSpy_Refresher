# NB: __init__ is the constructor for the class

class Shape: 
    def __init__(self, color, filled):
        self.color = color 
        self.filled = filled 
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'Empty'}")
        
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
        
class Square(Shape): 
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width
    def describe(self):
        print(f"\nThis is a {self.color} square")
        super().describe()
        
circle = Circle("red", True, 4)
#using kwargs
circle1 = Circle(color="red", filled=True, radius=4)
print(circle.filled)
print(circle1.color)
circle.describe()

square = Square("blue", True, 5)
square.describe()
