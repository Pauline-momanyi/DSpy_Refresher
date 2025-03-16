# Polymorphism - Many forms
# Ways to achieve: 
#     Inheritance: 
#     Duck typing 

#with inheritance 
class Shape:
    pass 
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self): 
        return self.side**2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*(self.radius**2)

square = Square(4) #here a square is both a Square and a shape 
circle = Circle(4) #here a circle is both a Circle and a shape but not a square

shapes = [Square(2), Circle(2)]

for shape in shapes:
    print(f'Area is {shape.area()} cm')
    
    
#with ducktyping
# objects must have the min necessary attr or methods, i.e. if it looks like and quacks like a duck then it is a duck
class Animal:
    def alive(self):
        print(True)
        
class Dog(Animal):
    def speak(self):
        print('WOOOOW')

class Car:
    def speak(self):  #I can treat it like an animal even if it's not cause it has this attr
        print('HORN!')
        
animals=[Dog(), Car()]
for animal in animals:
    animal.speak()
        