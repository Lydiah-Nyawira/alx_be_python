#Obtain the current date and time from datetime module
from datetime import datetime, timedelta

# Function to display current date
def display_current_datetime():
    # Get current date and time
    current_datetime = datetime.now()

    # Format current date and time
    formatted_date_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date_time}")

# Function to calculate a Future Date
def calculate_future_date():
    current_date = datetime.now
    days = int(input("Enter the number of days to add to the current date: ")) #Prompt the user
    future_date = current_date + timedelta(days=days)

    #Format future date
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date:  {formatted_future_date}")

# Execute script
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()               