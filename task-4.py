
# Task-8
#creat a python class called circle with constructor.
class Circle:
    # constructor
    def __init__(self):
        # initializing instance variable
        self.num = [10, 501, 22, 37, 100, 999, 87, 351]

    # a method
    def read_number(self):
        print(self.num)

# creating object of the class. This invokes constructor
obj = Circle()

# calling the instance method using the object obj
obj.read_number()

#creating proper member variables inside the task
class MyClass:
    # Private class variable
    __pi = 3.141

    # Public instance variable
    a = 33

    # Private method
    def __privMeth(self):
        print("I'm inside class MyClass")

    # Public method
    def hello(self):
        print("Private Variable value: ", MyClass.a)

# Creating an object of the class
foo = MyClass()

# Calling the public method
foo.hello()

# Accessing the public class variable
print(foo.a)

#creating two class methods area and perimeter which are going to calculate area and perimeter

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        # Area of a circle is πr²
        return self.radius**2 * 3.141

    def perimeter(self):
        # Perimeter (Circumference) of a circle is 2πr
        return 2 * self.radius * 3.141

# Creating a new Circle object with radius 7
NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())