import math

# This function calculates the area of a circle given its radius
def calculate_circle_area(radius):
    # Calculate the area using the formula: Area = π * r^2
    area = math.pi * (radius ** 2)
    return area

# Main part of the program
if __name__ == "__main__":
    # Get the radius from the user
    radius = float(input("Enter the radius of the circle: "))
    
    # Calculate the area of the circle
    area = calculate_circle_area(radius)
    
    # Print the area of the circle
    print(f"The area of the circle with radius {radius} is {area:.2f}.")
