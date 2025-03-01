# Abstract class = cannot be instantiated on its own, meant to be subclassed i.e. meant to be used by children 

#ABC - Abstract Base Classes
from abc import ABC, abstractmethod 

class Vehicle(ABC):
    #means you can't create a vehicle object directly, and all methods defined here must be used by children classes
    @abstractmethod
    def go(self):
        pass 
    @abstractmethod
    def stop(self):
        pass 
    
class Car(Vehicle):
    def go(self):
        print ("Drive Car")
        
    def stop(self):
        print("Stop Car")
              
car1 = Car()
car1.go()

class Motorcycle(Vehicle):
    def go(self):
        print ("Ride Motorcycle")
        
    def stop(self):
        print("Stop motorcycle")
        
motorcycle1 = Motorcycle()
motorcycle1.go()