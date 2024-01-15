# Program to demonstrate working with tuples in Python
 

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Access elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
subset_tuple = my_tuple[1:4]
print("Subset tuple:", subset_tuple)

# Concatenate tuples
new_tuple = my_tuple + (6, 7, 8)
print("Concatenated tuple:", new_tuple)

# Tuple unpacking
a, b, c, *rest = new_tuple
print("Unpacked variables:", a, b, c)
print("Remaining elements:", rest)

# Check if an element exists in a tuple
element_to_check = int(input("Enter an element to check in the tuple: "))
if element_to_check in new_tuple:
    print(f"{element_to_check} is present in the tuple.")
else:
    print(f"{element_to_check} is not present in the tuple.")
