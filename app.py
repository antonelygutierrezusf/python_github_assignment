# Welcome message to confirm the program is running
print("Welcome to my Python program!")

# Ask the user for input
hours = input("How many hours did you study today? ")

# Try converting input to float, exit if invalid
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculate weekly study hours
weekly_hours = hours * 7

# Display result clearly
print(f"You are on track to study {weekly_hours} hours this week.")