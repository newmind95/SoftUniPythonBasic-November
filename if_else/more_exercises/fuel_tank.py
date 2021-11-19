type_of_fuel = input()      # Text - "Diesel", "Gasoline", "Gas"
liters_fuel_in_tank = int(input())

result = ""

if type_of_fuel == "Diesel":
    if liters_fuel_in_tank >= 25:
        result = "You have enough diesel."
    else:
        result = "Fill your tank with diesel!"
elif type_of_fuel == "Gasoline":
    if liters_fuel_in_tank >= 25:
        result = "You have enough gasoline."
    else:
        result = "Fill your tank with gasoline!"
elif type_of_fuel == "Gas":
    if liters_fuel_in_tank >= 25:
        result = "You have enough gas."
    else:
        result = "Fill your tank with gas!"
else:
    result = "Invalid fuel!"

print(result)