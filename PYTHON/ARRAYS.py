
from typing import List, Union

#1. function to add integer values of an array.
def sum_array(arr: List[int]) -> int:
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

arr = [10, 20, 30, 40]
print("Sum of all integer values in array:", sum_array(arr))

# 2. function to calculate the average value of an array of integers.
def cal_average(num: List[int]) -> float:
    sum_num = 0
    for i in num:
        sum_num += i
    avg = sum_num / len(num)
    return avg


print("The average is", cal_average([10, 21, 32, 43, 54]))

# 3. program to find the index of an array element.
def find_index(arr: List[int], element: int) -> int:
    return arr.index(element) if element in arr else -1


arr = [1, 3, 5, 3, 1, 2, 6, 5, 3, 8, 6, 9]
print("Index of 3:", find_index(arr, 3))
print("Index of 9:", find_index(arr, 9))
print("Index of 8:", find_index(arr, 8))

# 4. function to test if array contains a specific value.
def contains_value(arr: List[int], value: int) -> bool:
    return value in arr


arr = [4, 5, 45, 40, 50]
print("Element exists:", contains_value(arr, 5))

# 5. function to remove a specific element from an array.
def remove_element(arr: List[int], value: int) -> List[int]:
    return [i for i in arr if i != value]


arr = [44, 55, 0, 15, 19, 5, 4]
print("Array after removing 0:", remove_element(arr, 0))

# 6. function to copy an array to another array.
def copy_array(arr: List[Union[int, str]]) -> List[Union[int, str]]:
    return arr.copy()


arr = ['R', 'A', 'M', 'A', 'R']
print("Copied array:", copy_array(arr))

# 7. function to insert an element at a specific position in the array.
def insert_element(arr: List[int], position: int, value: int) -> List[int]:
    arr.insert(position, value)
    return arr


arr = [101, 303, 404, 505, 606, 707, 808, 909]
print("Array after inserting 202 at index 1:", insert_element(arr, 1, 202))

# 8.function to find the minimum and maximum value of an array.
def min_max_array(arr: List[int]) -> (int, int): # type: ignore
    return min(arr), max(arr)


arr = [100, 3, 3000, 20, 500, 9999, 10000, 10003]
min_val, max_val = min_max_array(arr)
print("The minimum value is:", min_val)
print("The maximum value is:", max_val)

#9. function to reverse an array of integer values.
def reverse_array(arr: List[int]) -> List[int]:
    return arr[::-1]


arr = [9, 8, 7, 6, 5]
print("Reversed array:", reverse_array(arr))

# 10. function to find the duplicate values of an array.
def find_duplicates(arr: List[int]) -> List[int]:
    duplicates = []
    for i in range(len(arr)):
        for k in range(i + 1, len(arr)):
            if arr[i] == arr[k] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates


arr = [21, 11, 31, 13, 11]
print("Duplicate elements in the given array:", find_duplicates(arr))

#11. program to find the common values between two arrays.
def common_elements(arr1: List[Union[int, str]], arr2: List[Union[int, str]]) -> List[Union[int, str]]:
    return list(set(arr1).intersection(arr2))


arr = ['R', 'A', 'M', 'A', 'R']
arr1 = ['V', 'R', 'P']
print("Common values in the given arrays:", common_elements(arr, arr1))

# 12. method to remove duplicate elements from an array.
def remove_duplicates(arr: List[int]) -> List[int]:
    final_arr = []
    for i in arr:
        if i not in final_arr:
            final_arr.append(i)
    return final_arr


arr = [11, 22, 33, 11, 44, 55]
print("Array after removing duplicates:", remove_duplicates(arr))

# 13. method to find the second largest number in an array.
def second_largest(arr: List[int]) -> int:
    arr = list(set(arr))  # Removing duplicates
    arr.sort()
    return arr[-2] if len(arr) >= 2 else None


arr = [101, 404, 202, 909, 606, 505, 808, 303, 707]
print("Second largest number:", second_largest(arr))


# 14. method to find the number of even numbers and odd numbers in an array.
def count_even_odd(arr: List[int]) -> (int, int): # type: ignore
    evennumbers = 0
    oddnumbers = 0
    for i in arr:
        if i % 2 == 0:
            evennumbers += 1
        else:
            oddnumbers += 1
    return evennumbers, oddnumbers


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evennumbers, oddnumbers = count_even_odd(arr)
print("Even numbers in the given array:", evennumbers)
print("Odd numbers in the given array:", oddnumbers)

# 15. function to get the difference of the largest and smallest value.
def difference_largest_smallest(arr: List[int]) -> int:
    return max(arr) - min(arr)


arr = [10, 6, 11, 13, 14]
print("Difference of largest and smallest value:", difference_largest_smallest(arr))

# 16. method to verify if the array contains two specified elements (12, 23).
def contains_two_elements(arr: List[int], elem1: int, elem2: int) -> bool:
    return elem1 in arr and elem2 in arr


arr = [1, 12, 19, 23, 33, 54]
print("Array contains 12 and 23:", contains_two_elements(arr, 12, 23))

# 17.program to remove the duplicate elements and return the new array.
def remove_duplicates_return_array(arr: List[int]) -> List[int]:
    return list(set(arr))


arr = [11, 22, 33, 11, 44, 55]
print("Array after removing duplicates:", remove_duplicates_return_array(arr))