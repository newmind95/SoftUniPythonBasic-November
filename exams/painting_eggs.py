size_of_eggs = input()
color_of_eggs = input()
number_of_batches = int(input())
result = ""

if size_of_eggs == "Large":

    if color_of_eggs == "Red":
        price_of_batches = 16
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs
    elif color_of_eggs == "Green":
        price_of_batches = 12
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs
    elif color_of_eggs == "Yellow":
        price_of_batches = 9
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs
    
elif size_of_eggs == "Medium":

    if color_of_eggs == "Red":
        price_of_batches = 13
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs
    elif color_of_eggs == "Green":
        price_of_batches = 9
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs
    elif color_of_eggs == "Yellow":
        price_of_batches = 7
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs
    
elif size_of_eggs == "Small":

    if color_of_eggs == "Red":
        price_of_batches = 9
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs
    elif color_of_eggs == "Green":
        price_of_batches = 8
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs
    elif color_of_eggs == "Yellow":
        price_of_batches = 5
        price = number_of_batches * price_of_batches
        costs = price * 0.65
        result = "%.2f leva." % costs

print(result)
