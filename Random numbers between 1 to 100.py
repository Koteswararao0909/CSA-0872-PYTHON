import random

# This function generates a random number between 1 and 100
def generate_random_number():
    # Use random.randint to generate a random integer between 1 and 100
    random_number = random.randint(1, 100)
    return random_number

# Main part of the program
if __name__ == "__main__":
    # Generate a random number
    random_number = generate_random_number()
    
    # Print the random number
    print(f"The random number between 1 and 100 is: {random_number}")
