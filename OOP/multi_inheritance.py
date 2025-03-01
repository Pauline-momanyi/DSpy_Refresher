# # Multiple - inherit from more than 1 parent class
# class Prey:
#     def flee(self):
#         print("This animal is fleeing")

# class Predator: 
#     def hunt(self):
#         print("This animal is hunting") 

# class Rabbit(Prey):
#     pass 

# class Hawk(Predator): 
#     pass

# class Fish(Prey, Predator): #inherits from more than 1 parent
#     pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# hawk.hunt()
# fish.flee()
# fish.hunt()

# Multi-level inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
        
class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal): 
    def hunt(self):
        print("This animal is hunting") 

class Rabbit(Prey):
    pass 

class Hawk(Predator): 
    pass

class Fish(Prey, Predator): #inherits from more than 1 parent
    pass

rabbit = Rabbit("chichi")
hawk = Hawk("chocho")
fish = Fish("chuchu")

hawk.hunt()
fish.flee()
fish.hunt()
fish.eat()
