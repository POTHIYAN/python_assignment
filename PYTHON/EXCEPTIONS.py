class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class DummyClass:
    def __init__(self):
        self.existing_field = "I exist"

def generate_arithmetic_exception():
    result = 1 / 0
    print(result)

def handle_arithmetic_exception():
    try:
        result = 1 / 0
        print(result)
    except ZeroDivisionError as e:
        print(f"Caught an arithmetic exception: {e}")

def method_that_throws():
    raise ValueError("This method throws an exception")

def multiple_catch_blocks():
    try:
        result = 1 / 0
        print(result)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

def throw_custom_exception():
    raise Exception("This is a custom exception message")

def trigger_custom_exception():
    raise MyCustomException("This is my custom exception")

def with_finally_block():
    try:
        result = 1 / 0
        print(result)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    finally:
        print("This is the finally block, it always runs")

def generate_arithmetic_exception_direct():
    result = 1 / 0
    print(result)

def generate_file_not_found_exception():
    try:
        with open('nonexistent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

def generate_class_not_found_exception():
    try:
        import nonexistent_module  # type: ignore
    except ImportError as e:
        print(f"Caught ImportError (similar to ClassNotFoundException): {e}")

import os

def generate_io_exception():
    try:
        os.remove('nonexistent_file.txt')
    except OSError as e:
        print(f"Caught OSError (similar to IOException): {e}")

def generate_no_such_field_exception():
    dummy = DummyClass()
    try:
        print(dummy.nonexistent_field)
    except AttributeError as e:
        print(f"Caught AttributeError (similar to NoSuchFieldException): {e}")

def main():
    print("1. Uncomment to generate Arithmetic Exception without exception handling")
    # generate_arithmetic_exception()

    print("\n2. Handle Arithmetic Exception using try-catch block")
    handle_arithmetic_exception()

    print("\n3. Call method that throws exception")
    try:
        method_that_throws()
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\n4. Multiple catch blocks")
    multiple_catch_blocks()

    print("\n5. Throw custom exception")
    try:
        throw_custom_exception()
    except Exception as e:
        print(f"Caught Exception: {e}")

    print("\n6. Custom exception")
    try:
        trigger_custom_exception()
    except MyCustomException as e:
        print(f"Caught MyCustomException: {e}")

    print("\n7. Finally block")
    with_finally_block()

    print("\n8. Generate Arithmetic Exception")
    try:
        generate_arithmetic_exception_direct()
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\n9. Generate FileNotFoundException")
    generate_file_not_found_exception()

    print("\n10. Generate ClassNotFoundException")
    generate_class_not_found_exception()

    print("\n11. Generate IOException")
    generate_io_exception()

    print("\n12. Generate NoSuchFieldException")
    generate_no_such_field_exception()

if __name__ == "__main__":
    main()
