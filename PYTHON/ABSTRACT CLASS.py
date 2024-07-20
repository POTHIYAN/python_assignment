from abc import ABC, abstractmethod

# Step 1: Create an abstract class with abstract and non-abstract methods
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    def description(self):
        print("This is a shape")

# Step 2: Create a subclass for the abstract class
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Overriding the abstract method
    def area(self):
        return self.width * self.height

    def description(self):
        print("This is a rectangle")

# Step 3 and 4: Create an instance of the child class in the child class and call both abstract and non-abstract methods
class TestRectangle:
    def __init__(self):
        self.rect = Rectangle(10, 20)
    
    def call_methods(self):
        print(f"Area: {self.rect.area()}")   # Calling the abstract method
        self.rect.description()              # Calling the non-abstract method

# Driver code
# Step 2: Creating an object of the child class and accessing the non-abstract methods
rect_obj = Rectangle(10, 20)
rect_obj.description()

# Step 3 and 4: Creating an instance of the child class in the child class and calling methods
test_rect = TestRectangle()
test_rect.call_methods()
