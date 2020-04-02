# Here we learn about Class Function return
class course:
    def __init__(self, name):
        self.name="Python"
        self.students=[]
    def add_students(self,student):
        self.students.append(student)  
    def students_count(self):
        return len(self.students)    

# c1=course("Python")
# c1.add_students("Umer")
# c1.add_students("Farooq")
# print(c1.students)
# print(c1.students_count())