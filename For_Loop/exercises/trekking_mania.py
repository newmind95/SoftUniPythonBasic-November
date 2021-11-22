number_of_group = int(input())
total_climbers = 0
climbing_musala = 0
climbing_monblan = 0
climbing_kilimanjaro = 0
climbing_k2 = 0
climbing_everest = 0

for group in range(1, number_of_group + 1):
    number_of_climbers_in_group = int(input())

    if number_of_climbers_in_group <= 5:
        climbing_musala += number_of_climbers_in_group
    elif number_of_climbers_in_group <= 12:
        climbing_monblan += number_of_climbers_in_group
    elif number_of_climbers_in_group <= 25:
        climbing_kilimanjaro += number_of_climbers_in_group
    elif number_of_climbers_in_group <= 40:
        climbing_k2 += number_of_climbers_in_group
    else:
        climbing_everest += number_of_climbers_in_group

total_climbers = climbing_musala + climbing_monblan + climbing_kilimanjaro \
                 + climbing_k2 + climbing_everest

percentage_musala = climbing_musala / total_climbers * 100
percentage_monblan = climbing_monblan / total_climbers * 100
percentage_kilimanjaro = climbing_kilimanjaro / total_climbers * 100
percentage_k2 = climbing_k2 / total_climbers * 100
percentage_everest = climbing_everest / total_climbers * 100
print(f"{percentage_musala:.2f}%")
print(f"{percentage_monblan:.2f}%")
print(f"{percentage_kilimanjaro:.2f}%")
print(f"{percentage_k2:.2f}%")
print(f"{percentage_everest:.2f}%")