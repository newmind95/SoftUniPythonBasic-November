number = int(input())
left_sum = 0
right_sum = 0

for numbers in range(number * 2):
    current_number = int(input())

    if numbers < number:
        left_sum += current_number
    else:
        right_sum += current_number

if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    difference = abs(right_sum - left_sum)
    print(f"No, diff = {difference}")