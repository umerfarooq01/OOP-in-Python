# Here we learn about Python Private Properties
class course:
    def __init__(self, name):
        # When we want to private a property in python we just use __ in the start of the property name
        self.__name="Python"
        self.students=[]
    def add_students(self,student):
        self.students.append(student)  
    def students_count(self):
        return len(self.students)    
c1=course("Python")
# Now the name varable name is not shown in c1. 
print(c1.students)        