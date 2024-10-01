class Student:
    def __init__(self, name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
     
    
class Course:
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
            
    def get_average_grade(self):
        total = 0
        
        for student in self.students:
           total += student.get_grade()
        return total/len(self.students)
    
s1 = Student("grace", 10, 80)
s2 = Student("gra", 12, 60)
s3 = Student("g", 9, 90)

course = Course("Bio", 2)
print(course.add_students(s1))
print(course.add_students(s2))
print(course.add_students(s3))
print (course.students[0].name)

print(course.get_average_grade())

