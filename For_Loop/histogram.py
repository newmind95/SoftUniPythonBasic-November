n = int(input())

p_one = 0
p_two = 0
p_three = 0
p_four = 0
p_five = 0

for number in range(0, n):
    current_number = int(input())

    if current_number < 200:
        p_one += 1
    elif 200 <= current_number <= 399:
        p_two += 1
    elif 400 <= current_number <= 599:
        p_three += 1
    elif 600 <= current_number <= 799:
        p_four += 1
    else:
        p_five += 1

print(f"{p_one/n*100:.2f}%")
