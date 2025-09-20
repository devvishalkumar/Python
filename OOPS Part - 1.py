# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.

# Class & Object 

"""class Student:
    name = "vishal kumar"

s1 = Student()
print(s1.name)"""

"""class Car:           # Creating class 
    color = "blue"
    brand = "mercedes"

car1 = Car()        # creating object
print(car1.color)
print(car1.brand)
"""
# __init__ Function (Constructor)

# All classes have a function called __init__(),
# which is always executed when the object is being initiated.

'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student,",self.name)

    def get_marks(self):
        return self.marks

s1 = Student("vishal kumar", 95)
s1.welcome()
print(s1.get_marks())'''

# Let's Practice

# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    @staticmethod       # Static methods :- methods that don't use the self parameter (work at class level)
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi", self.name, "your avg score is :", sum/3)
            

s1 = Student("vishal kumar", [99, 98, 97])
s1.get_avg()
s1.hello()


