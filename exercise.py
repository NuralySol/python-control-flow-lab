# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

#! f strings seem to be more usefull in this case.
#! Control logic and fucntion declaration 
def check_letter():
    letter = input("Please enter a letter: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print(f"'{letter}' is not a valid letter.")
        return

    vowels = "aeiou"

    if letter in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

#! Function declarition (importantly input fields follow the waterfall logic: Promtps in Node.js?)

def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        # should be useful since you do not want to enter negative numbers
        if age < 0:
            print("Age cannot be negative.")
            return

        voting_age = 18

        if age >= voting_age:
            print(f"You are {age} years old and eligible to vote!")
        else:
            print(f"You are {age} years old and not old enough to vote. You need to be at least {voting_age} to be able to vote")
    # Error checker for invalid entries
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function
check_voting_eligibility()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Prompt the user for inputs
    is_cold = input("Is it cold? (yes/no): ").lower()
    is_raining = input("Is it raining? (yes/no): ").lower()

    #! ( == is a strict equals like in JS but still can reassigned which is weird!)
    # Provide clothing advice based on the conditions
    if is_cold == "yes" and is_raining == "yes":
        print("Wear a waterproof coat.")
    elif is_cold == "yes" and is_raining == "no":
        print("Wear a warm coat.")
    elif is_cold == "no" and is_raining == "yes":
        print("Carry an umbrella.")
    elif is_cold == "no" and is_raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input, please answer with 'yes' or 'no'.")

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

#! Everything to the right of the = sign is an objec in Python. OOP programming for you. 
def determine_season():
    # Prompt the user to enter the month and day
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    day = int(input("Enter the day of the month: "))

    # Define the months for each season
    winter = ('Dec', 'Jan', 'Feb', 'Mar')
    spring = ('Mar', 'Apr', 'May', 'Jun')
    summer = ('Jun', 'Jul', 'Aug', 'Sep')
    fall = ('Sep', 'Oct', 'Nov', 'Dec')

    # Determine the season based on the month and day
    # Boolean logic to determine in which month go with each season of the year
    #! Chaining boolean always looks weird, and it is much easier to read than in JS. 
    if (month == 'Dec' and day >= 21) or (month in winter and month != 'Mar') or (month == 'Mar' and day <= 19):
        season = "Winter"
    elif (month == 'Mar' and day >= 20) or (month in spring and month != 'Jun') or (month == 'Jun' and day <= 20):
        season = "Spring"
    elif (month == 'Jun' and day >= 21) or (month in summer and month != 'Sep') or (month == 'Sep' and day <= 21):
        season = "Summer"
    elif (month == 'Sep' and day >= 22) or (month in fall and month != 'Dec') or (month == 'Dec' and day <= 20):
        season = "Fall"
    else:
        season = "an invalid date. Please enter a valid month and day."

    # Print the season
    #! f strings seem to be much more intuitive in Python and template literals in JS.
    print(f"{month} {day} is in {season}.")

# Call the function
determine_season()


