# print(__name__)
# object - instance of a class to imply bundle of related attr - features, and methods(functions) - actions
# class - blueprint to design structure of object

class Car:
    
    car_type = "suv" #class var
    num_cars = 0
    
    def __init__(self, model, year, cost):
        self.model = model #Instance variable
        self.year = year 
        self.cost = cost 
        Car.num_cars += 1 #adds ater every initialization
        
    def show_price(self):
        print (f'cost is {self.cost}')
    def drive(self):
        print (f'You are driving a {self.year} {self.model}')
           
lexus = Car('lexus', '2023', 5600)
print(lexus.cost)
lexus.show_price()
lexus.drive()
print(Car.car_type)
print (lexus.car_type) #you can use class variables using the class itself
print (Car.num_cars)

camry = Car('camry', '2023', 2600)
print (Car.num_cars)