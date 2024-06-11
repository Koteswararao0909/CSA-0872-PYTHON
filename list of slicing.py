def main():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Basic slicing examples
    print("Original list:", numbers)
    print("First three elements:", numbers[:3])
    print("Elements from index 3 to 6:", numbers[3:7])
    print("Last three elements:", numbers[-3:])
    print("Every second element:", numbers[::2])
    print("Reverse list:", numbers[::-1])

    # Modifying list using slicing
    numbers[1:4] = [20, 30, 40]
    print("List after modifying elements from index 1 to 3:", numbers)

if __name__ == "__main__":
    main()
