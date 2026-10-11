cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("price is 20 rupees")
else:
    print("Unknown cup size")


# Practise Program: Sugar level selection
sugar_level = input("Enter sugar level (0-3): ")

if sugar_level == "0":
    print("No sugar added")
elif sugar_level == "1":
    print("1 spoon of sugar added")
elif sugar_level == "2":
    print("2 spoons of sugar added")
elif sugar_level == "3":
    print("3 spoons of sugar added")
else:
    print("Unknown sugar level")