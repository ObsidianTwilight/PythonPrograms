class Student:#every class must have constructor
    

    #Constructor of class student
    def __init__(self,Name,Age,Course): #parameterized constructor
        self.name = Name
        self.age = Age
        self.course = Course


    def greet(self):
        print("My name is " + self.name)        

kiran = Student("Kiran",20,"BBA")
"""print(kiran.name)
print(kiran.age)
print(kiran.course)"""



kiran.greet()