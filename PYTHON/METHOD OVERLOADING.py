class Example:
    # Method with the same name but different number of parameters (same type)
    def method(self, a, b=None):
        if b is not None:
            print(f"Method with two parameters: a={a}, b={b}")
        else:
            print(f"Method with one parameter: a={a}")

    # Method with the same name but different number of parameters (different types)
    def method_overload(self, a, b=None):
        if isinstance(a, int) and b is None:
            print(f"Method with one integer parameter: a={a}")
        elif isinstance(a, int) and isinstance(b, str):
            print(f"Method with one integer and one string parameter: a={a}, b={b}")
        elif isinstance(a, int) and isinstance(b, int):
            print(f"Method with two integer parameters: a={a}, b={b}")
        else:
            print("Method with unsupported parameters")

    # Method with the same name and same number of parameters (same type)
    def method_same(self, a, b):
        if a == b:
            print(f"Both parameters are the same: a={a}, b={b}")
        else:
            print(f"Parameters are different: a={a}, b={b}")

def main():
    ex = Example()

    # Example 1: Method with the same name but different number of parameters (same type)
    print("Example 1:")
    ex.method(10)
    ex.method(10, 20)

    # Example 2: Method with the same name but different number of parameters (different types)
    print("\nExample 2:")
    ex.method_overload(10)
    ex.method_overload(10, "hello")
    ex.method_overload(10, 20)

    # Example 3: Method with the same name and same number of parameters (same type)
    print("\nExample 3:")
    ex.method_same(10, 10)
    ex.method_same(10, 20)

if __name__ == "__main__":
    main()
