# Define Global Conversion Factors:
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implement Conversion Functions:
def convert_to_celsius(celsius):
    fahrenheit = celsius * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit
def convert_to_fahrenheit(farenheit):
    celsius = (farenheit - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    return celsius 

# User Interaction:
def main():
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature} is {converted_temp}")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}. is {converted_temp}")
    else:
        print("Invalid temperature. Please enter a numeric value.")

#Execute script
if __name__ ==  "__main__":
    main()