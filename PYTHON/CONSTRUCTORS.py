class BaseClass:
    def __init__(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"BaseClass Constructor with two arguments: a={a}, b={b}")
        elif a is not None:
            print(f"BaseClass Constructor with one argument: a={a}")
        else:
            print("BaseClass Default Constructor")

class DerivedClass(BaseClass):
    def __init__(self, a=None, b=None):
        if a is not None and b is not None:
            super().__init__(a, b)
        elif a is not None:
            super().__init__(a)
        else:
            super().__init__()
        print("DerivedClass Constructor")

class AccessModifiers:
    def __init__(self):
        self.public_attribute = "Public"
        self._protected_attribute = "Protected"
        self.__private_attribute = "Private"
        print("AccessModifiers Constructor")

    def display_attributes(self):
        print(f"Public Attribute: {self.public_attribute}")
        print(f"Protected Attribute: {self._protected_attribute}")
        print(f"Private Attribute: {self.__private_attribute}")

class ConstructorAttributes:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def display(self):
        print(f"Attribute 1: {self.attr1}, Attribute 2: {self.attr2}")

def main():
    # 1. Instantiate the class to call all the constructors
    print("\nCalling BaseClass Constructors:")
    obj1 = BaseClass()
    obj2 = BaseClass(10)
    obj3 = BaseClass(10, 20)
    
    print("\nCalling DerivedClass Constructors:")
    obj4 = DerivedClass()
    obj5 = DerivedClass(30)
    obj6 = DerivedClass(40, 50)
    
    # 3. Apply private, public, protected and default access modifiers to the constructor
    print("\nAccess Modifiers Example:")
    access_modifiers = AccessModifiers()
    access_modifiers.display_attributes()

    # 4. Attributes of a Constructor
    print("\nConstructor Attributes Example:")
    constructor_attributes = ConstructorAttributes("Value1", "Value2")
    constructor_attributes.display()

if __name__ == "__main__":
    main()
