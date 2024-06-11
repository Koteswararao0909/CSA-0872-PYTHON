# This function converts a temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Use the formula: F = C * 9/5 + 32
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Main part of the program
if __name__ == "__main__":
    # Get the Celsius temperature from the user
    celsius = float(input("Enter the temperature in Celsius: "))
    
    # Convert the Celsius temperature to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    # Print the Fahrenheit temperature
    print(f"The temperature in Fahrenheit is {fahrenheit:.2f} degrees.")
