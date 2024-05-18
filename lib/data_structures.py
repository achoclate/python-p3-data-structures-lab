spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_str = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level_str}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

# Example
print(get_names(spicy_foods))  # ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']
print(get_spiciest_foods(spicy_foods))  # [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}]
print_spicy_foods(spicy_foods)  # Prints formatted spicy food details
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))  # {'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}
print_spiciest_foods(spicy_foods)  # Prints only the spiciest foods
print(get_average_heat_level(spicy_foods))  # Average heat level
print(create_spicy_food(spicy_foods, {"name": "Sriracha", "cuisine": "Thai", "heat_level": 8}))  # Adds new spicy food and prints the updated list
