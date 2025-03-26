# @propert decorator: Define a method as a property. Can be accessed as an attribute. Gives you getter, setter and deleter options
#setter - implemented when you initialize 
#NB: Remember a decorator is an already existing function, and you can create your own decorators

class Rectangle:
    def __init__(self, width, height):
        #underscore to denote private attr
        self._width = width 
        self._height = height
        
    #getters
    @property 
    #this will act as getter methods
    def width(self):
        return self._width    
    
    @property
    def height(self):
        return self._height 
    
    #setters
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print (f"{new_width} is an invalid width")
    
    @height.setter
    def height(self, new_height):
        if new_height>0:
            self._height = new_height
        else:
            print (f"{new_height} is an invalid height")
            
    #deleter
    @width.deleter 
    def width(self):
        del self._width 
        print("Width deleted")
        
    
    
rectangle = Rectangle(4, 5)

#using the setters
rectangle.width = -4
rectangle.height = 6

#using deleter
# del rectangle.width

#using getter
print(rectangle.width) #without property decorator you use () unless you want to return location in memory
# print (rectangle.height())
print (rectangle.height)
