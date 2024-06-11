# This function calculates the average of a list of numbers
def calculate_average(numbers):
    # Check if the list is empty to avoid division by zero
    if len(numbers) == 0:
        return 0
    # Calculate the sum of the numbers
    total = sum(numbers)
    # Calculate the average by dividing the total by the number of elements
    average = total / len(numbers)
    return average

# Example usage:
numbers_list = [1, 2, 3, 4, 5]
average_result = calculate_average(numbers_list)
print("The average is:", average_result)
