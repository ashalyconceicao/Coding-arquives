# This example program is meant to demonstrate errors.

print("Welcome to the error program")  # Missing parentheses in print function

# Add a new line
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old"  # Changed '==' to '=' for assignment
age = int(age_Str.split()[0])  # Extract the number part from the string
print("I'm " + str(age) + " years old.")  # Convert age to str for concatenation

# Variables declaring additional years and printing the total years of age
years_from_now = 3  # Converted to an integer without quotes
total_years = age + years_from_now  # Now correctly adds two integers

print("The total number of years:" + str(total_years))  # Print the calculated total_years

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12  # Corrected the variable name to total_years
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")  # Convert total_months to str for concatenation

# HINT, 330 months is the correct answer
