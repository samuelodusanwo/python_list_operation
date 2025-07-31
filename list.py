"""
    Create an empty list called my_list.
    Append the following elements to my_list: 10, 20, 30, 40.
    Insert the value 15 at the second position in the list.
    Extend my_list with another list: [50, 60, 70].
    Remove the last element from my_list.
    Sort my_list in ascending order.
    Find and print the index of the value 30 in my_list.
"""


# 1. Create an empty list called my_list.
my_list = []
print(f"Initial list: {my_list}")

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After appending 10, 20, 30, 40: {my_list}")
# Expected: [10, 20, 30, 40]

# 3. Insert the value 15 at the second position in the list (index 1).
my_list.insert(1, 15)
print(f"After inserting 15 at index 1: {my_list}")
# Expected: [10, 15, 20, 30, 40]

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print(f"After extending with [50, 60, 70]: {my_list}")
# Expected: [10, 15, 20, 30, 40, 50, 60, 70]

# 5. Remove the last element from my_list.
my_list.pop() # Removes the last element (70 in this case)
print(f"After removing the last element: {my_list}")
# Expected: [10, 15, 20, 30, 40, 50, 60]

# 6. Sort my_list in ascending order.
my_list.sort()
print(f"After sorting in ascending order: {my_list}")
# Expected: [10, 15, 20, 30, 40, 50, 60]
# (In this specific sequence, the list was already in sorted order by chance before this step,
# so its visual order doesn't change, but the sort method was called.)

# 7. Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print(f"The index of the value 30 in my_list is: {index_of_30}")
# Expected: The index of the value 30 in my_list is: 3