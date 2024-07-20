#1.Print Name Program#
print("POTHIYAN RAMAR")

#2.Comment Program#
print("# - SINGLE LINE COMMENT")
print("'''  ''' - MULTI LINE COMMENT ")

#3.Data Types Program
my_int=10
my_bool=True
my_char='A'
my_float=3.14
my_double=3.14159

print("Integer:", my_int)
print("Boolean:", my_bool)
print("Character:", my_char)
print("Float:", my_float)
print("Double:" , my_double)

#4.Local And Global Variables Program

# Global variable
x = 10

def my_function():
    # Local variable with the same name
    x = 20
    print("Inside function:")
    print("Local x:", x)
    print("Global x:", globals()['x'])

print("Outside function:")
print("Global x:", x)
my_function()
print("Outside function:")
print("Global x:", x)


''' We define a global variable x with value 10.
- Inside the my_function, we define a local variable x with value 20.
- We print the values of both local and global x inside the function using globals()['x'] to access the global variable.
- We print the value of the global x outside the function before and after calling the function.

This demonstrates that the local variable x inside the function does not affect the global variable x outside the function, and vice versa. The scope of the variables is as follows:

- Global x: accessible from anywhere in the program
- Local x: only accessible within the my_function scope'''