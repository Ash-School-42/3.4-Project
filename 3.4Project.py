from datetime import datetime
# This program will ask the user for an input off of a simple menu
# then print the result with the datetime.

print("jamash0376 Spreadsheet Automation Menu")
print("Choose a number from the following options")

menu_options = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
    ]
    
for option in menu_options:
    print(option)
        

# The next line retreives the inputted option and stores the variable
# called <number>.
number = input("Enter your number: ")

if number == "1":
    print("You selected 1 at ",str(datetime.now()))
elif number == "2":
    print("You selected 2 at ",str(datetime.now()))
elif number == "3":
    print("You selected 3 at ",str(datetime.now()))
else:
    print("Error: Invalid choice selected.")

# Creates the convertData function.
def convertData(weight):
    return weight / 2.205

# Creates the getInput fucntion
def getInput():
    number = int(input("How many entries are you inputting?: "))
    for num in range(number):
        date = input("Enter a date: ")
        weight = float(input("Enter weight in pounds: "))
        # ConvertData takes weight in pounds and returns converted weight
        # in kilograms
        convertedWeight = convertData(weight)
        print(f'The following was saved at {datetime.now()}:')
        print(f'{date},{weight},{convertedWeight}')
    print("All data has been saved!")

if number == "1":
    getInput()
else:
    print("Error: The chossen functionality is not implemented yet")
