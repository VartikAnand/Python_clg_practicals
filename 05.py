# Program to create, append, and remove elements from a list in Python

# Create a list
my_list = [1, 2, 3, 4, 5]

# Print the original list
print("Original List:", my_list)

# Append elements to the list
new_elements = [6, 7, 8]
my_list.extend(new_elements)

# Print the list after appending
print("List after Appending:", my_list)

# Remove elements from the list
element_to_remove = int(input("Enter an element to remove from the list: "))
if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"List after Removing {element_to_remove}:", my_list)
else:
    print(f"{element_to_remove} not found in the list.")

# Clear the entire list
my_list.clear()
print("List after Clearing:", my_list)
