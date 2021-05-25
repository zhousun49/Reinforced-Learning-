def readtext(price, food, location):
    ret = []
    file1 = open('restaurantDatabase.txt', 'r')
    for i in file1:
        spl = i.split("\t")
        #All alise 
        if (price == "any") and (food == "any") and (location == "any"):
            if spl[0] != 'RESTAURANT_NAME':
                ret.append(spl)
        elif (price == "any") and (food == "any"):
            if (location in spl[4]):
                ret.append(spl)
        elif (food == "any") and (location == "any"): 
            if (price in spl[3]):
                ret.append(spl)
        elif (price == "any") and (location == "any"): 
            if (food in spl[2]):
                ret.append(spl)
        elif (location == "any"):
            if (spl[2] == food) and (spl[3] == price):
                ret.append(spl)
        elif (price == "any"):
            if (spl[2] == food) and (location in spl[4]):
                ret.append(spl)
        elif (food == "any"):
            if (location in spl[4]) and (spl[3] == price):
                ret.append(spl)
        else:
            if (spl[2] == food) and (spl[3] == price) and (location in spl[4]):
                ret.append(spl)
    print("I found {} restaurants matching your query. ".format(len(ret)), ''.join(["{} is a {} {} restaurant in {}. The telephone number is {}. ".format(i[0], i[3], i[2], i[4], i[1]) for i in ret]))

# readtext("expensive", "Japanese", "any")