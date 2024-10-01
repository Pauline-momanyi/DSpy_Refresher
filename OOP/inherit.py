class Pet:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def what(self):
        print("This is a pet")
    
class Cat(Pet):
    def show(self):
        print(f"My cat is {self.name} and its {self.age}")
        
    # def what(self):
    #     print("This is a cat") 

class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        print(f"My dog is {self.name} and its {self.age} and {self.color} in color")
     
      


cat1 = Cat("pp", 14)
cat1.show()
cat1.what()

dog1 = Dog("dd", 14, "brown")