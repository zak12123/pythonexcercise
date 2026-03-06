# We use a loop to keep asking until the data is valid
while True:
    try:
        # Try to convert the input to an integer
        age = int(input("Please enter your age: "))

        # If the line above works, we break out of the loop
        break

    except ValueError:
        # If the 'int()' conversion crashes, the code jumps here
        print("Error: That is not a valid number. Please use digits only.")

print(f"Thank you, age {age} has been recorded.")

