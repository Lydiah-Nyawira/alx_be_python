# Prompt the user
number = int(input("Enter a number to see its multiplication table: "))
X = number

# Generate and Print the Multiplication Table:
for Y in range (1, 11):
    Z = X * Y
    print(f"{X} * {Y} = {Z}")