age = int(input("Please enter your age: "))

# Categorize age-related messages based on the entered age
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")

# The program prompts the user for their age and performs specific actions based on the entered age.
# It utilizes if-elif-else statements to categorize the age-related messages in a hierarchical manner.
# Proper indentation (4 spaces per level) and concise comments, adhering to PEP8 guidelines, have been applied.
