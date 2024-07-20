# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
students = {
    101: "RAM",
    102: "RAGHU",
    103: "MITHRAN",
    104: "DADA",
    105: "BABY"
}

# 1.1 Adding the values in dictionary
students[106] = "LOVE"
students.update({107: "JACK"})

print("After adding values:")
print(students)

# 1.2 Updating the values in dictionary
students[101] = "RAM"
students.update({102: "ROBERT"})

print("\nAfter updating values:")
print(students)

# 1.3 Accessing the value in dictionary
print("\nAccessing values:")
print(f"Student with ID 103: {students[103]}")
print(f"Student with ID 104: {students.get(104)}")

# 1.4 Create a nested loop dictionary
nested_dict = {
    'class1': {
        201: "KAMESH",
        202: "KALISH"
    },
    'class2': {
        203: "JASS",
        204: "BOSS"
    }
}

print("\nNested dictionary:")
print(nested_dict)

# 1.5 Access the values of nested loop dictionary
print("\nAccessing values in nested dictionary:")
for class_name, students_in_class in nested_dict.items():
    print(f"\nClass: {class_name}")
    for student_id, student_name in students_in_class.items():
        print(f"ID: {student_id}, Name: {student_name}")

# 1.6 Print the keys present in a particular dictionary
print("\nKeys in students dictionary:")
print(students.keys())

print("\nKeys in nested dictionary:")
for class_name in nested_dict:
    print(f"Class: {class_name}, Keys: {nested_dict[class_name].keys()}")

# 1.7 Delete a value from a dictionary
if 105 in students:
    del students[105]
if 106 in students:
    students.pop(106)

print("\nAfter deleting values:")
print(students)

# Run the main function to execute the above operations
if __name__ == "__main__":
    # The main block for executing the script
    pass
