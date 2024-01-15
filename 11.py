import fibonacci_module

# Get user input for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Use the function from the module to generate Fibonacci numbers
fibonacci_numbers = fibonacci_module.generate_fibonacci(n)

# Print the result
print(f"Fibonacci Numbers up to {n}: {fibonacci_numbers}")
