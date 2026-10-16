menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea)


#Practise code

vehicles = [
    "Petrol",
    "Diesel",
    "Hybrid",
    "Hybrid CNG",
    "Electric",
    "Petrol CNG",
    "Hybrid Electric"
]

hybrid_vehicles = [filtered_vehicle for filtered_vehicle in vehicles if "Hybrid" in filtered_vehicle]

print(hybrid_vehicles)