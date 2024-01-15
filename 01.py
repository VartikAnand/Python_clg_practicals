# Program to demonstrate different number data types in Python




# Integer
integer_number = int(input("Enter an Integer: "))
print("Integer:", integer_number)

# Float
float_number = float(input("Enter a Float: "))
print("Float:", float_number)

# Complex
real_part = float(input("Enter the real part of a Complex number: "))
imaginary_part = float(input("Enter the imaginary part of a Complex number: "))
complex_number = complex(real_part, imaginary_part)
print("Complex:", complex_number)

# Arithmetic operations
sum_result = integer_number + float_number
print("Sum:", sum_result)

# Type conversion
float_to_int = int(float_number)
print("Float to Int:", float_to_int)

# Operations with complex numbers
complex_addition = complex_number + (1 - 2j)
print("Complex Addition:", complex_addition)

# Type of the result
result_type = type(complex_addition)
print("Result Type:", result_type)
