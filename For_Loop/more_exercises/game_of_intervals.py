number_of_moves_in_the_game = int(input())
result = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for number in range(1, number_of_moves_in_the_game + 1):

    numbers = int(input())

    if 0 <= numbers <= 9:
        from_0_to_9 += 1
        result += numbers * (20 / 100)
    elif 10 <= numbers <= 19:
        from_10_to_19 += 1
        result += numbers * (30 / 100)
    elif 20 <= numbers <= 29:
        from_20_to_29 += 1
        result += numbers * (40 / 100)
    elif 30 <= numbers <= 39:
        from_30_to_39 += 1
        result += 50
    elif 40 <= numbers <= 50:
        from_40_to_50 += 1
        result += 100
    elif numbers < 0 or numbers > 50:
        invalid_numbers += 1
        result /= 2

percentage_from_0_to_9 = (from_0_to_9 * 100 / number_of_moves_in_the_game)
percentage_from_10_to_19 = (from_10_to_19 * 100 / number_of_moves_in_the_game)
percentage_from_20_to_29 = (from_20_to_29 * 100 / number_of_moves_in_the_game)
percentage_from_30_to_39 = (from_30_to_39 * 100 / number_of_moves_in_the_game)
percentage_from_40_to_50 = (from_40_to_50 * 100 / number_of_moves_in_the_game)
percentage_invalid_numbers = (invalid_numbers * 100 / number_of_moves_in_the_game)

print(f"{result:.2f}")
print(f"From 0 to 9: {percentage_from_0_to_9:.2f}%")
print(f"From 10 to 19: {percentage_from_10_to_19:.2f}%")
print(f"From 20 to 29: {percentage_from_20_to_29:.2f}%")
print(f"From 30 to 39: {percentage_from_30_to_39:.2f}%")
print(f"From 40 to 50: {percentage_from_40_to_50:.2f}%")
print(f"Invalid numbers: {percentage_invalid_numbers:.2f}%")