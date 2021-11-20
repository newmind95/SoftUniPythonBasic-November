type_of_fuel = input()
fuel_quantity = float(input())
club_card = input()

price_gasoline_per_liter = 2.22
price_diesel_per_liter = 2.33
price_gas_per_liter = 0.93

total_price_gasoline = 0
total_price_diesel = 0
total_price_gas = 0
result = ""

if club_card == "Yes":
    price_gasoline_per_liter -= (18 / 100)
    price_diesel_per_liter -= (12 / 100)
    price_gas_per_liter -= (8 / 100)

if 20 <= fuel_quantity <= 25:
    total_price_gasoline = fuel_quantity * price_gasoline_per_liter
    total_price_gasoline = total_price_gasoline - (total_price_gasoline * (8 / 100))

    total_price_diesel = fuel_quantity * price_diesel_per_liter
    total_price_diesel = total_price_diesel - (total_price_diesel * (8 / 100))

    total_price_gas = fuel_quantity * price_gas_per_liter
    total_price_gas = total_price_gas - (total_price_gas * (8 / 100))
elif fuel_quantity >= 25:
    total_price_gasoline = fuel_quantity * price_gasoline_per_liter
    total_price_gasoline = total_price_gasoline - (total_price_gasoline * (10 / 100))

    total_price_diesel = fuel_quantity * price_diesel_per_liter
    total_price_diesel = total_price_diesel - (total_price_diesel * (10 / 100))

    total_price_gas = fuel_quantity * price_gas_per_liter
    total_price_gas = total_price_gas - (total_price_gas * (10 / 100))
else:
    total_price_gasoline = fuel_quantity * price_gasoline_per_liter
    total_price_diesel = fuel_quantity * price_diesel_per_liter
    total_price_gas = fuel_quantity * price_gas_per_liter

if type_of_fuel == "Gasoline":
    result = f"{total_price_gasoline:.2f} lv."
elif type_of_fuel == "Diesel":
    result = f"{total_price_diesel:.2f} lv."
elif type_of_fuel == "Gas":
    result = f"{total_price_gas:.2f} lv."

print(result)