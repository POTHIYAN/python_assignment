#1. program to print “Bright IT Career” ten times using for loop
for i in range(10):
    print("Bright IT Career")

#2. program to print 1 to 20 numbers using the while loop.
i = 1
while i <= 20:
    print(i)
    i += 1


#3. Program to equal operator and not equal operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a == b)
print(a != b)


#4.program to print the odd and even numbers.
num = int(input("Enter a number: "))
for i in range(1, num+1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

#5.program to print largest number among three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"{a} is the largest")
elif b >= a and b >= c:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")


#6.program to print even number between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#7.program to print 1 to 10 using the do-while loop statement.
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break


#8.program to find Armstrong number or not
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp != 0:
    digit = temp % 10
    sum += digit ** len(str(num))
    temp //= 10
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

#9.program to find the prime or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

#10.program to palindrome or not

num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp != 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if num == reverse:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")


#11.check whether a number is EVEN or ODD using switch
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#12.gender (Male/Female) program according to given M/F using switch

gender = input("Enter gender (M/F): ")
if gender.upper() == 'M':
    print("Male")
elif gender.upper() == 'F':
    print("Female")
else:
    print("Invalid input")


