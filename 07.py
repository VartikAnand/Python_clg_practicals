# Create a dictionary
person_info = {'name': 'Vartik', 'age': 21, 'country': 'India'}

# Access values in the dictionary
print("Name:", person_info['name'])
print("Age:", person_info['age'])
print("Country:", person_info['country'])

# Update a value in the dictionary
person_info['age'] = 22
print("Updated Age:", person_info['age'])

# Add a new key-value pair to the dictionary
person_info['occupation'] = 'Student'
print("Updated Dictionary:", person_info)

# Remove a key-value pair from the dictionary
key_to_remove = input("Enter a key to remove from the dictionary: ")
if key_to_remove in person_info:
    del person_info[key_to_remove]
    print(f"Dictionary after removing {key_to_remove}:", person_info)
else:
    print(f"{key_to_remove} not found in the dictionary.")

# Check if a key exists in the dictionary
key_to_check = input("Enter a key to check in the dictionary: ")
if key_to_check in person_info:
    print(f"{key_to_check} is present in the dictionary.")
else:
    print(f"{key_to_check} is not present in the dictionary.")
