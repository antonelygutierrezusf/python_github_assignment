print("Welcome to my Python program!")
hours = input("How many hours did you study today? ")
# Task 3: Convert input to float and calculate weekly hours
try:
    hours = float(hours)
    weekly_hours = hours * 7
except ValueError:
    print("Please enter a valid number.")
    exit()