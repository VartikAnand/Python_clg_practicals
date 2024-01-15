from greet_module import greet ,hru

# Get user input for the name
name = input("Enter your name: ")

# Use the function from the module
greet_msg1 = greet(name)
greet_msg2 = hru()

# Print the result
print(greet_msg1 ,"&",greet_msg2)

