# Number of rows in the pattern
rows = 3


# Upper part of the pattern
print("*")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower part of the pattern
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print("*")
