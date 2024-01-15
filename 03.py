# Program to create, concatenate, and print a string
# Also, demonstrates accessing a sub-string


# Create a string
str1 = input("Enter the first string: ")

# Concatenate strings
str2 = input("Enter the second string to concatenate: ")
result_string = str1 + str2

# Print the result string
print("Result String:", result_string)

# Access sub-string
start_index = int(input("Enter the starting index number: "))
end_index = int(input("Enter the ending index number: "))
substring = result_string[start_index:end_index]

# Print the sub-string
print("Sub-string:", substring)
