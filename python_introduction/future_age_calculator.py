#Prompt the user for their current age
current_age = int(input("How old are you?"))

#Calculate the future age assuming the current year is 2023
future_year = 2050
current_year = 2023
years_to_add = future_year - current_year
age = current_age + years_to_add
 
 #Print results
 print(f"In 2050, you will be {age} years old")