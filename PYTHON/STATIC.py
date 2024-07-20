class MyClass:
    static_var = 42  # static variable

# 1. Access through class
print("Access through class:", MyClass.static_var)

# 2. Access through instance
instance = MyClass()
print("Access through instance:", instance.static_var)

# 3. Change within the instance
instance.static_var = 99  # changing through instance
print("Instance static_var:", instance.static_var)  # instance-specific change
print("Class static_var:", MyClass.static_var)  # class variable remains unchanged

# 4. Change within the class
MyClass.static_var = 99
print("Access through class after change:", MyClass.static_var)

# Access through instance to see the effect
instance = MyClass()
print("Access through instance after class change:", instance.static_var)
