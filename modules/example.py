import math
pi = math.pi

def cube(val):
    return val * val
def area(radius):
    return pi*radius**2 
def circum(radius):
    return 2*pi*radius

# print(help("modules")) #list of available modules
print(__name__)