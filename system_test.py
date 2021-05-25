import csv
from re import search
from readtext import readtext
#Read csv file and assign the action with states
dic = {}
with open('./policy.csv', 'r' ) as theFile:
    reader = csv.reader(theFile)
    for line in reader:
        values = ""
        for j in range(len(line)):
            # print(len(line))
            if j != len(line)-1:
                values = values + line[j]
            else: 
                action = line[j]
        dic[values] = action
dic.pop('FOOD_TYPE_FILLEDPRICE_FILLEDLOCATION_FILLEDFOOD_TYPE_CONFPRICE_CONFLOCATION_CONF')
print("Length of dictionary: ", len(dic))
#Initialize food types, price types and location types
food_type = ["empty", 'any', 'Italian', 'Japanese', 'Chinese', 'Mexican', 'Greek']
price = ['empty', 'any', 'cheap','medium-priced' ,'expensive']
locations = ['empty', 'any', 'Marina Del Rey', 'Venice', 'Santa Monica', 'Korea Town', 'Playa Vista', 'Hollywood']

get_food = "What type of food do you want? \n"
get_price = "How expensive a restaurant do you want? \n"
get_location = "Where would you like the restaurant to be located? \n"

initialization = "000000"
result = "111111"
init = [0, 0, 0, 0, 0, 0]
while initialization != result: 
    sys_action = dic[initialization] 
    if sys_action == "REQUEST_PRICE":
        p = input(get_price)
        for j in price:
            if p != "empty":
                if search(j.lower(), p.lower()):
                    p = j
                    # print("Price: ", p)
                    init[1] = 1
                    break
        #Position of initialization
    elif sys_action == "REQUEST_FOOD_TYPE":
        food = input(get_food)
        for j in food_type:
            if food != "empty":
                if search(j.lower(), food.lower()):
                    food = j
                    # print("Food Type: ", food)
                    init[0] = 1
                    break
    elif sys_action == "REQUEST_LOCATION":
        location = input(get_location)
        for j in locations:
            if location != "empty":
                if search(j.lower(), location.lower()):
                    location = j
                    # print("Location Type: ", location)
                    init[2] = 1
                    break
    elif sys_action == "EXPLICIT_CONFIRM_LOCATION":
        location_conf = input('Ok, you said you wanted a restaurant in {}, correct? \n'.format(location))
        if search("yes", location_conf.lower()):
            init[5] = 1
        elif search("no", location_conf.lower()):
            init[2] = 0
    elif sys_action == "EXPLICIT_CONFIRM_PRICE":
        price_conf = input('Ok, you said you wanted a {} restaurant, correct? \n'.format(p))
        if search("yes", price_conf.lower()):
            init[4] = 1
        elif search("no", price_conf.lower()):
            init[1] = 0
    elif sys_action == "EXPLICIT_CONFIRM_FOOD_TYPE":
        food_conf = input('Ok, you said you wanted a {} restaurant, correct? \n'.format(food))
        if search("yes", food_conf.lower()):
            init[3] = 1
        elif search("no", food_conf.lower()):
            init[0] = 0
    lst = [str(x) for x in init]
    initialization = "".join(lst)
    # print("Next state: ", initialization)
#Output Quesry results
readtext(p, food, location)