class Person:
    number = 0 #specific to class i.e class attribute
    def __init__(self, name) -> None:
        self.name = name
        
    # class methosd: Don't reference self but the class itself
    
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