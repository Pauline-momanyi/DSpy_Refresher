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
        def __init__(self, name, position):
            self.name = name
            self.position = position
            
        def get_details(self):
            return f"{self.name} {self.position}"
    
    def __init__(self, company_name):
        self.company_name = company_name 
        self.employees = []
        
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]
        
        
company1 = Company("msft")
company1.add_employee('popo', 'dev')
company1.add_employee('lili', 'nurse')

for employee in company1.list_employees():
    print(employee)