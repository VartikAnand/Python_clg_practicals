#calculate electric bill
from electric_bill_module import ElectricBill

# Take input from the user
name = input("Enter customer name: ")
address = input("Enter customer address: ")
units = float(input("Enter units consumed: "))

# Create an instance of ElectricBill
customer = ElectricBill(name, address, units)

# Calculate the bill
bill = customer.calculate_bill()

# Print the result
print(f"\nElectric Bill for {customer.customer_name} at {customer.customer_address}:")
print(f"Units Consumed: {customer.units_consumed}")
print(f"Total Bill: rupees{bill}")
