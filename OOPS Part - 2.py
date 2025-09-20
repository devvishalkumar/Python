# del keyword

"""class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("vishal kumar")
print(s1.name)

del s1.name
print(s1.name)"""

# Private attributes & methods : Conceptual implementation in python
#   Private attributes & methods are meant to be used only within the class
#   and are not accessible from outside the class.

"""class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")
        
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())"""

# Inheritance :
#   When one class (child/derived) derives the properties & methods of
#   another class (parent/base).

# Single Inheritance

"""class Car:
    color = "Red"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("mercedes")
car2 = ToyotaCar("fortuner")

car1.start()
car2.stop()
print(car1.color)
"""
# Multi-level Inheritance

"""class Car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()"""

# Multiple Inheritance

"""class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)"""

# Super method

"""class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name, type):
        self.name = name
        super().__init__(type)
        super().start()
        

car1 = ToyotaCar("mercedes","electric")
print(car1.name)
print(car1.type)
"""
# class method:
#   A class method is bound to the class & receives the class an implicit first argument.
#   Note :- static method can't access or modify class state & generally for utility.

"""class Person:
    name = "anonymous"
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Vishal kumar")
print(p1.name)"""

# Property:
#   We are @property decorator on any method in the class to use the method as a propert.

"""class Student:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math
    
    @property
    def percentage(self):
        return str((self.phy + self.che + self.math) / 3) + "%"

stu1 = Student(86,95,75)
print(stu1.percentage)

stu1.che = 90
print(stu1.percentage)"""

# Polymorphism : Operator Overloading
#   When the same operator is allowed to have different meaning according to the context.

"""class Complex:
    def __init__(self, real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i",self.img,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(9, 5)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()"""

# Let's Practice

# Define a circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a perimeter() method of the class which allow you to calculate the perimeter of the circle.

"""class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())"""

# Define a Employee class with attributes role, department & salary. This cass also a
# showDetails() method.
#   Create an Engineer class that inherits properties from Employee & has additional
# attributes : name & age.

"""class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000")

engg1 = Engineer("Vishal kumar", 18)
engg1.showDetails()"""

# Create a class called Order which stores item & its price.
# Use Dunder function _ _gt_ _() to convey that:
#       order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order("chips",20)
odr2 = Order("tea",15)

print(odr1 > odr2)


