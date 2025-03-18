#Instance methods : operations on instances of the class. The normal ones I have been doing
#Static methods: Best for utility functions that do not need access to class data. Uses a decorator - @staticmethod

class Math:
    # static methods don't change. They don't act on anything so they don't take the self arg
    
    @staticmethod
    def add5(x):
        return x+5
    
    @staticmethod
    def pr():
        print ("run")
        
        
# print(Math.add5(10))
# Math.pr()

class Employee: 
    def __init__(self, name, position):
        self.name = name
        self.position = position 
    @staticmethod
    def is_valid_pos(position):
        valid_pos = ["Manager", "Cook"]
        return position in valid_pos 
    
print(Employee.is_valid_pos("Cook"))

employee1 = Employee('popo', 'dev')
employee2 = Employee('lili', 'Manager')

print(Employee.is_valid_pos(employee2.position))