# Prompt the user
length = int(input("Enter the size of the pattern: "))

# Initialize variable
row = 0

# Draw the pattern
while row < length:
    column = 0 # Start with the first columnin each row
    for j in range(length): # Loop through each column
            print("*", end="") # Print asterik without moving to a new line
    print() # Move to a new line after each row
    row += 1  