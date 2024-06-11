# This program demonstrates the use of comments in Python

def check_even_or_odd(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from the user
# Convert the input to an integer
number = int(input("Enter a number: "))

# Call the function with the user's number and store the result
result = check_even_or_odd(number)

# Print the result
print(f"The number {number} is {result}.")

# End of the program
