# Prompt the user
task = input("Describe the task: ")
priority = input("Enter the task priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time_bound?yes/no: ").strip().lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = "do it immediately"
    case "medium":
        reminder = "do it as soon as possible"
    case "low":
        reminder = ", consider completing it when you have free time"
    case _:
        print("Invalid priority level entered")
        
#Check if the task is time bound
if time_bound == "yes":
    print("This task requires immediate action")
elif time_bound == "no":
    print("This task does not require immediate action")
else:
    print("Invalid input for time_bound")    
            
# Provide a Customized Reminder
print(f"{task} is a {priority} priority task {reminder}")