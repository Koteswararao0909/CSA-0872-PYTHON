def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
number = int(input("Enter a number: "))
result = check_even_or_odd(number)
print(f"The number {number} is {result}.")
