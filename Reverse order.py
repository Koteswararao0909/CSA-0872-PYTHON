def reverse_string(string):
    return string[::-1]

def main():
    user_input = input("Enter a string: ")
    reversed_string = reverse_string(user_input)
    print("Reversed string:", reversed_string)

if __name__ == "__main__":
    main()
