flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]


for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")
    
print(f"Out side of loop")

# Practice Program: Coffee Flavours
flavours = ["Espresso", "Out of Stock", "Latte", "Discontinued", "Cappuccino"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found") 

