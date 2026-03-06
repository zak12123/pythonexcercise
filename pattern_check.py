
staff_id = input("Enter ID (must start with ST-): ")

# While the input does NOT follow the pattern...
while not staff_id.startswith("ST-"):
    print("Invalid Format! Use ST- at the start.")
    staff_id = input("Enter ID: ")

print("Format accepted.")