# Define all classes in a single script for demonstration

# Private fields and methods
class A:
    def __init__(self):
        self.__private_field = "This is a private field"

    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        print("This is a public method")
        print("Accessing private field:", self.__private_field)
        self.__private_method()

    def main(self):
        print("\nPrivate access within A:")
        try:
            print(self.__private_field)
        except AttributeError:
            print("Cannot access private field directly")

        try:
            self.__private_method()
        except AttributeError:
            print("Cannot call private method directly")

        self.public_method()

class B(A):
    def __init__(self):
        super().__init__()

    def access_private(self):
        print("\nPrivate access from B:")
        try:
            print(self.__private_field)
        except AttributeError:
            print("Cannot access private field in subclass")

        try:
            self.__private_method()
        except AttributeError:
            print("Cannot call private method in subclass")

    def public_method(self):
        print("\nPublic method in B:")
        super().public_method()

# Protected fields and methods
class AProtected:
    def __init__(self):
        self._protected_field = "This is a protected field"

    def _protected_method(self):
        print("This is a protected method")

    def public_method(self):
        print("\nPublic method in AProtected:")
        print("Accessing protected field:", self._protected_field)
        self._protected_method()

class BProtected(AProtected):
    def __init__(self):
        super().__init__()

    def access_protected(self):
        print("\nAccessing protected fields and methods in BProtected:")
        print("Protected field:", self._protected_field)
        self._protected_method()

# Public fields and methods
class APublic:
    def __init__(self):
        self.public_field = "This is a public field"

    def public_method(self):
        print("\nPublic method in APublic:")
        print("Accessing public field:", self.public_field)

class BPublic(APublic):
    def __init__(self):
        super().__init__()

    def access_public(self):
        print("\nAccessing public fields and methods in BPublic:")
        print("Public field:", self.public_field)
        self.public_method()

# Demonstration
def main():
    # Testing private members
    print("Testing private members:")
    a = A()
    a.main()

    b = B()
    b.access_private()
    b.public_method()

    # Testing protected members
    print("\nTesting protected members:")
    a_protected = AProtected()
    a_protected.public_method()

    b_protected = BProtected()
    b_protected.access_protected()

    # Testing public members
    print("\nTesting public members:")
    a_public = APublic()
    a_public.public_method()

    b_public = BPublic()
    b_public.access_public()

if __name__ == "__main__":
    main()
