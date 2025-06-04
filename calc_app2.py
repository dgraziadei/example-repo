# ********* TASK 17 **********

# A simple calulator which takes user input and saves all calculations in a seperate text file 

# Welcome text and calculator explanation 
print("\n---------------------------------------------------------------\n")
print("Welcome to our SIMPLE CALCULATOR!\n")
print("This calculator allows you to use the following calculations:\n + = Addition\n - = Subtraction\n / = Division\n * = Multiplication\n")

print("Please choose one of the following: ")
print("1. Perform a calculation")
print("2. Show previous equations")
print("3. Quit")
print("\n---------------------------------------------------------------\n")
# Define a function and provide defensive programming:
def calculation_simple():
    """
    Handles the calculations of the user and saving the content into a file 

    Arg:
    num1, symbol and num2 are the user inputs for the calculation 

    Returns:
    The calculation result
    """
    try: 
        # Get user imput regarding calculation:
        num1 = float(input("\nWhat number in your calculation?: "))
        symbol = input("Please enter the correct symbol for your calculation (allowed symbols: +, -, / or *): ")
        num2 = float(input("Please enter the second number of your calculaion (which follows the symbol): "))
        
        # Use an if-loop to provide infromation of each calculation to the function
        if symbol == "+":
            result = num1 + num2
        elif symbol == "-":
            result = num1 - num2
        elif symbol == "/":
            if num2 == 0: # Defensive programming so that ZeroDivisionError does not occur 
                print("You cannot divide by 0")
                return
            result = num1 / num2
        elif symbol == "*":
            result = num1 * num2 
        else: # Defensive Programming so that ValueError does not occur 
            print("Invalid symbol! Please choose from the list above.")
            return
        
        # Provide code for what to do with calculation:
        calculation = f"{num1} {symbol} {num2} = {result}"
        print("\nResult: ", calculation)
        print("\n---------------------------------------------------------------\n")

        # Open a specified file and safe calculations there: 
        with open("equations.txt", "a") as file:
            file.write(calculation + "\n")
    
    # Defensive Programming exception option to ensure people input numeric values 
    except ValueError:
        print("Ivalid input. Please choose numeric values for your two numbers")

# Create another function for showing previous calculations
def previous_calculation():
    """
    Handles the opening of the files and reading the content

    Arg:
    contents = reading the file

    Returns:
    All previosuly saved equations form the specific file
    """
    try:
        with open("equations.txt", "r") as file:
            contents = file.read()
            if contents:
                print("\nPrevious equations:\n")
                print(contents)
            else:
                print("No previous equations found.")

    #Defensive Programming in case File does not exist: 
    except FileNotFoundError: 
        print("No equations file found yet. Try doing some calculations first.")

# Return output to user based on function and heir choice whether they want to calculate or see previous calculations
while True:
        choice = input("Enter your choice (1, 2, or 3): ")

# Specific user choices: 
        if choice == "1":
            calculation_simple()
        elif choice == "2":
            previous_calculation()
        elif choice == "3":
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


    


