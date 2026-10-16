favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais }
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)

#practise code

city_places = {
    "Pune":["Shaniwar Wada", "Sinhagad Fort", "Pataleshwar Cave Temple"],
    "Mumbai":["Gateway of India", "Marine Drive", "Juhu Beach", "Sinhagad Fort"]
}

unique_spots = {spot for places in city_places.values() for spot in places}

print(unique_spots)