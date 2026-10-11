staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")

# Practice Program: Staff Eligibility Check
staff = [("Alice", 20), ("Bob", 19), ("Charlie", 22)]
for name, age in staff:
    if age < 21:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")