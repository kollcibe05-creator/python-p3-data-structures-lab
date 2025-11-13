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

# def sort_list (value):
#     return (value["heat_level"] > 5)
#     pass

def get_names(spicy_foods):
    my_list = []  # !!
    for item in spicy_foods: # !!
        # print(my_list.append(item["name"] )) 
        my_list.append(item["name"]) # !!
    return my_list  # !!
    pass

def get_spiciest_foods(spicy_foods):
    my_list = []
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5 :
            my_list.append(spicy_food)
    return my_list   
    pass
print(get_spiciest_foods(spicy_foods))
def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        times = spicy_food["heat_level"]
        emoji = "🌶"
        emoji_output =  emoji * times  
        to_print = f"{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {emoji_output}"            #uncomment
        print(to_print)                                                                                       #uncomment
    pass

# print_spicy_foods(spicy_foods)   // i am getting an error on output but the test passes


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
    pass

# print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            times = spicy_food["heat_level"]
            emoji = "🌶"
            emoji_output =  emoji * times  
            to_print = f"{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {emoji_output}"            #uncomment
            print(to_print)                                                                                      #uncomment         
    pass

def get_average_heat_level(spicy_foods):
    my_array = []
    for spicy_food in spicy_foods:
        my_array.append(spicy_food["heat_level"])        
    total = sum(my_array)
    length = len(my_array)
    average = total/length
    return average
    pass


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    print(spicy_foods)
    return spicy_foods
    pass

