# Here we learn how to create Python Class Functions
class course:
    def __init__(self, name):
        self.name="Python"
        self.students=[]
    def add_students(self,student):
        self.students.append(student)   

# c1=course("Python")
# c1.add_students("Umer")
# c1.add_students("Farooq")
# print(c1.students)
# print(len(c1.students))