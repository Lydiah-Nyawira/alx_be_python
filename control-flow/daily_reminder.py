# daily_reminder.py

# Prompt the user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium piority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"
    case _:
        print("Invalid priority level entered")
        
#Check if the task is time bound
if time_bound.lower() == 'yes':
    reminder += " it requires immediate action"
elif time_bound == "no":
    reminder += " it does not require immediate action"
else:
    print("Invalid input for time_bound")    
            
# Provide a Customized Reminder
print(f"Reminder: {reminder}")