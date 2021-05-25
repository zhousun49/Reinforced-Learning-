import random
def su_action(action):
    pos = 0.2
    if action == "request_food_type":
        if random.random() < 0.8:
            return "provide_food_type"
        else: 
            return "irrelevant"
    if action == "request_price":
        if random.random() < 0.8:
            return "provide_price"
        else: 
            return "irrelevant"
    if action == "request_location":
        if random.random() < 0.8:
            return "provide_location"
        else: 
            return "irrelevant"
    if action == "explicit_confirm_food_type":
        rand = random.random()
        if  rand < pos:
            return "confirm_pos_food_type"
        elif rand > 0.9: 
            return "irrelevant"
        else:
            return "confirm_neg_food_type"
    if action == "explicit_confirm_price":
        rand = random.random()
        if  rand < pos:
            return "confirm_pos_price"
        elif rand > 0.9: 
            return "irrelevant"
        else:
            return "confirm_neg_price"
    if action == "explicit_confirm_location":
        rand = random.random()
        if  rand < pos:
            return "confirm_pos_location"
        elif rand > 0.9: 
            return "irrelevant"
        else:
            return "confirm_neg_location"