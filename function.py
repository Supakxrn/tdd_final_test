def validate_weight(weight):
    if type(weight) != int:
        if type(weight) == str:
            return "input integer"
        elif weight >= 1 and weight <= 3000:
            return "input integer"
        else:
            return "out of range"
    elif weight >= 1 and weight <= 3000:
        return weight
    else:
        return "out of range"

#ราคาปาล์มน้ำมัน = 32
def display_cost(weight):
    cost = validate_weight(weight)
    if type(cost) == int:
        result = cost*32
        return result
    else:
        return cost