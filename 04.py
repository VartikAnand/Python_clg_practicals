#Python script that prints the current date in the specified format "Fri Oct 11"


from datetime import datetime

# Get the current date
current_date = datetime.now()

# Format the date as "Fri Oct 11"
formatted_date = current_date.strftime("%a %b %d")


# Explanation of date format:
# %a represents the abbreviated weekday name (e.g., Fri for Friday).
# %b represents the abbreviated month name (e.g., Oct for October).
# %d represents the day of the month as a zero-padded decimal number.

# Print the formatted date
print("Current Date:", formatted_date)
