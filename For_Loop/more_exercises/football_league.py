capacity_of_stadium = int(input())
number_of_all_fans = int(input())
fans_in_sector_a = 0
fans_in_sector_b = 0
fans_in_sector_v = 0
fans_in_sector_g = 0

for fan in range(1, number_of_all_fans + 1):

    fan_in_sector = input()

    if fan_in_sector == 'A':
        fans_in_sector_a += 1
    elif fan_in_sector == 'B':
        fans_in_sector_b += 1
    elif fan_in_sector == 'V':
        fans_in_sector_v += 1
    elif fan_in_sector == 'G':
        fans_in_sector_g += 1

percentage_of_fans_in_sector_a = (fans_in_sector_a / number_of_all_fans) * 100
percentage_of_fans_in_sector_b = (fans_in_sector_b / number_of_all_fans) * 100
percentage_of_fans_in_sector_v = (fans_in_sector_v / number_of_all_fans) * 100
percentage_of_fans_in_sector_g = (fans_in_sector_g / number_of_all_fans) * 100
average_of_all_fans = (number_of_all_fans / capacity_of_stadium) * 100

print(f"{percentage_of_fans_in_sector_a:.2f}%")
print(f"{percentage_of_fans_in_sector_b:.2f}%")
print(f"{percentage_of_fans_in_sector_v:.2f}%")
print(f"{percentage_of_fans_in_sector_g:.2f}%")
print(f"{average_of_all_fans:.2f}%")
