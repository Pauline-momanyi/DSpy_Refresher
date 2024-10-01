class Dog:
    def __init__(self, name, age) -> None:
        self.name = name #create an attribute of the class and name it name (the 1st)
        self.age = age
        print(name)
    
    def get_name(self):
        return self.name
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        
    
# class Cat:
#     def __init__(self, name) -> None:
#         self.myname = name
#         print(self.myname)
# cat1 = Cat('caat')   
        
dog1 = Dog('dooog', 24)
print(dog1.get_name())
print(dog1.get_age())
dog1.set_age(26)
print(dog1.get_age())
