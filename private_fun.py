# Here we learn about  Python Class Private Functions
class course:
    def __init__(self, name):
        # When we want to private a property in python we just use __ in the start of the property name
        self.__name="Python"
        self.students=[]
    def add_students(self,student):
        self.students.append(student)  
        self.__student_write(student)
    def students_count(self):
        return len(self.students)    
    def __student_write(self,student):
        print("Hello "+ student)    

c1=course("Python")
print(c1.add_students("Umer"))git 
