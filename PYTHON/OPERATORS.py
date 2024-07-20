#1.Arithmetic Operator Program
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    print(x + y)
elif operator == '-':
    print(x - y)
elif operator == '*':
    print(x * y)
elif operator == '/':
    if y != 0:
        print(x / y)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Error: Invalid operator")

#2.Increment And Decrement Operators Program
# Get initial value from user
a = int(input("Enter the initial value for a: "))

# Increment operations
a += 1
a = a + 1
print('The value of a after incrementing is', a)

# Decrement operations
a -= 1
a = a - 1
print('The value of a after decrementing is', a)

# Incremented for loop
print("\nINCREMENTED FOR LOOP")
for i in range(0, 5):
    print(i)

# Decremented for loop
print("\nDECREMENTED FOR LOOP")
for i in range(4, -1, -1):
    print(i)

#3 program to find the two numbers equal or not.
# Get the two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the numbers are equal
if num1 == num2:
  print("The numbers are equal")
else:
  print("The numbers are not equal")

#4.Relational Operators Program
# Get input from the user
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Print the results of the relational operators
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal to
print("a > b:", a > b)  # Greater than
print("a < b:", a < b)  # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

#5.Smaller And Larger Number Program
# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Determine the smaller and larger number
if num1 < num2:
  smaller = num1
  larger = num2
else:
  smaller = num2
  larger = num1

# Print the results
print("Smaller number:", smaller)
print("Larger number:", larger)
