# Prompt the user
Task = input("Describe the task: ")
Priority = input("Enter the task priority (high/medium/low): ").strip().lower()
Time_Bound = input("Is the task time_bound? (yes/no): ").strip().lower()

# Process the Task Based on Priority and Time Sensitivity
match Priority:
    case "high":
        reminder = "do it immediately"
    case "medium":
        reminder = "do it as soon as possible"
    case "low":
        reminder = ", consider completing it when you have free time"
    case _:
        print("Invalid priority level entered")
        
#Check if the task is time bound
if Time_Bound == "yes":
    print("This task requires immediate action")
elif Time_Bound == "no":
    print("This task does not require immediate action")
else:
    print("Invalid input for time_bound")    
            
# Provide a Customized Reminder
print(f"{Task} is a {Priority} priority task {reminder}")