from function import display_cost

input_weight = input()
try:
    try:
        input_weight = int(input_weight)
    except:
        input_weight = float(input_weight)
except:
    input_weight = str(input_weight)

result = display_cost(input_weight)
print(result)