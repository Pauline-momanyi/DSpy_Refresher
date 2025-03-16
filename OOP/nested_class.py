# nested class = class defined within another class # allows you to logically group closely related classes
# Encapsulate private details that are not relevant outside the class 
# Reduce possibility of naming conflicts


#example
# class Company:
#     class Employee:
#         print("This is the first class")
        
# class Nonprofit:
#     class Employee:
#         print("This is the second class")

class Company:
    class Employee:
        pass 
    def __init__(self, company_name):
        self.company_name = company_name 
        self.employees = []
        
    def add_employee:
        
        