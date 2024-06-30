# Prompt the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")

# Perform the calculation
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print(f"Error: Division by zero")
            result = None
    case _:
        print(f"Error: Invalid operation")

# Print output
if result is not None:
    print(f"The result is {result}")                