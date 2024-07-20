import re

# 1. Different ways of creating a string
str1 = 'Hello'
str2 = "World"
str3 = '''Hello
World'''
str4 = str(1234)

# 2. Concatenating two strings using + operator
concatenated = str1 + " " + str2
print("Concatenated string:", concatenated)

# 3. Finding the length of the string
length = len(str1)
print("Length of the string:", length)

# 4. Extract a string using Substring
substring = str1[0:5]  # Extracting 'Hello'
print("Substring:", substring)

# 5. Searching in strings using index()
index = str1.index("lo")
print("Index of 'lo':", index)

# 6. Matching a String Against a Regular Expression With matches()
pattern = r"Hello"
if re.match(pattern, str1):
    print("Pattern matches")
else:
    print("Pattern does not match")

# 7. Comparing strings
str3 = "Hello"
print("str1 equals str2:", str1 == str2)
print("str1 equals str3:", str1 == str3)

# 8. startsWith(), endsWith() and compareTo()
print("Starts with 'Hello':", str1.startswith("Hello"))
print("Ends with 'World':", str2.endswith("World"))
str2 = "Hello World"
print("str1 equals str2:", str1 == str2)

# 9. Trimming strings with strip()
str1 = "   Hello World   "
trimmed = str1.strip()
print("Trimmed string:", trimmed)

# 10. Replacing characters in strings with replace()
str1 = "Hello World"
replaced = str1.replace("World", "Python")
print("Replaced string:", replaced)

# 11. Splitting strings with split()
split_str = str1.split(" ")
print("Split string:", split_str)

# 12. Converting integer objects to Strings
num = 1234
str_num = str(num)
print("Converted integer to string:", str_num)

# 13. Converting to uppercase and lowercase
str1 = "Hello World"
upper = str1.upper()
lower = str1.lower()
print("Uppercase:", upper)
print("Lowercase:", lower)
