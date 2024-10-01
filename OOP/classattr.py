class Person:
    number = 0 #specific to class i.e class attribute
    def __init__(self, name) -> None:
        self.name = name
        
    # class method: Don't reference self but the class itself
    # You can use a method to call it but you dont have to
    
    @classmethod
    def get_number(cls):
        return cls.number
    
    @classmethod
    def add_person(cls):
        cls.number += 1
        return cls.number
        
p1 = Person("popo")
print (p1.number)
print (Person.number)  

print (Person.get_number())
print (Person.add_person())
print("End of first")

class Person1:
    number = 0 #specific to class i.e class attribute
    def __init__(self, name) -> None:
        self.name = name
        # the class method below can be used here
        Person1.add_person()
        
    # class method: Don't reference self but the class itself
    # You can use a method to call it but you dont have to
    
    @classmethod
    def get_number(cls):
        return cls.number
    
    @classmethod
    def add_person(cls):
        cls.number += 1
        return cls.number
        
p11 = Person1("popo")
print (p11.number)
print (Person1.number)  

print (Person1.get_number())
print (Person1.add_person())