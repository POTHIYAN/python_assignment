class A:
    def method1(self):
        print("A's method1")

    def method2(self):
        print("A's method2")

    def override_method(self):
        print("A's override method")

    data_member = "A's data member"


class B(A):
    def method3(self):
        print("B's method3")

    def method4(self):
        print("B's method4")

    def override_method(self):
        print("B's override method")

    data_member = "B's data member"


class C(B):
    def method5(self):
        print("C's method5")

    def method6(self):
        print("C's method6")

    def override_method(self):
        print("C's override method")

    data_member = "C's data member"


class Main:
    def main(self):
        # Creating objects
        a = A()
        b = B()
        c = C()

        # Calling methods of class A
        print("Calling methods of class A:")
        a.method1()
        a.method2()
        a.override_method()

        # Calling methods of class B
        print("\nCalling methods of class B:")
        b.method3()
        b.method4()
        b.override_method()

        # Calling methods of class C
        print("\nCalling methods of class C:")
        c.method5()
        c.method6()
        c.override_method()
# Runtime polymorphism with method overriding
        print("\nRuntime polymorphism with method overriding:")
        a_ref = B()
        a_ref.override_method()  # Output: B's override method

        a_ref = C()
        a_ref.override_method()  # Output: C's override method

        # Runtime polymorphism with data members
        print("\nRuntime polymorphism with data members:")
        a_ref = B()
        print(a_ref.data_member)  # Output: B's data member

        a_ref = C()
        print(a_ref.data_member)  # Output: C's data member


if __name__ == "__main__":
    main_obj = Main()
    main_obj.main()
