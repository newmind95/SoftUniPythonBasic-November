number_of_cargo = int(input())          # integer between [1...1000]
price_for_one_ton = 0                   # price for one ton - initialize to 0
price_for_minibus = 0                   # price for minibus - initialize to 0
price_for_truck = 0                     # price for truck - initialize to 0
price_for_train = 0                     # price for train - initialize to 0
total_cargo = 0                         # total cargo - initialize to 0
average_per_ton = 0                     # average per ton - initialize to 0
minibus = 0                             # number of minibuses - initialize to 0
truck = 0                               # number of trucks - initialize to 0
train = 0                               # number of trains - initialize to 0

for cargo in range(1, number_of_cargo + 1):

    tonnage_cargo = int(input())        # tonnage of cargo - integer between [1...1000]
    total_cargo += tonnage_cargo

    # Check whether tonnage of cargo is less than or equal to 3
    # if is true, then assign tonnage of cargo to number of minibuses
    # and compute the tonnage
    if tonnage_cargo <= 3:
        price_for_one_ton = 200
        price_for_minibus += tonnage_cargo * price_for_one_ton
        minibus += tonnage_cargo

    # Check whether tonnage of cargo is less than or equal to 3
    # if is true, then assign tonnage of cargo to number of trucks
    # and compute the tonnage
    elif tonnage_cargo <= 11:
        price_for_one_ton = 175
        price_for_truck += tonnage_cargo * price_for_one_ton
        truck += tonnage_cargo

    # if tonnage is greater than or equal to 12
    # assign tonnage of cargo to number of trucks
    # and compute the tonnage
    else:
        price_for_one_ton = 120
        price_for_train += tonnage_cargo * price_for_one_ton
        train += tonnage_cargo

average_per_ton = (price_for_minibus + price_for_truck + price_for_train) / total_cargo
minibus_percentage = (minibus / total_cargo) * 100
truck_percentage = (truck / total_cargo) * 100
train_percentage = (train / total_cargo) * 100
print(f"{average_per_ton:.2f}")
print(f"{minibus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")