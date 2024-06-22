#Prompt the user for their monthly income and their total monthly savings
monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

#Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#Calculate projected Annual Savings after one year with 5% interest
Projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Print results
print(f"Projected savings is {Projected_savings} and user's monthly savings is {monthly_savings}")