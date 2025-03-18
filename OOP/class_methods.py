#Class methods: Allow operations related to the class itself. Take cls(class) while object methods take self.
# uses a @classmethod decorator, and cls instead of self
# class methods: Class variables. Need to work on class data
# static methods: Utility fxns that dont need access to the class data
# instance methods: operations on instances of the class
    
class Student:
    #class variables
    count = 0
    gpa_total = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa 
        Student.count += 1
        Student.gpa_total += gpa
        
    @classmethod
    def get_count(cls):
        return cls.count
    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        return cls.gpa_total/cls.count
    
print (Student.get_count())
student1 = Student('popo', 2)
student2 = Student('popo', 2)
print (Student.get_count())
print(Student.get_average())