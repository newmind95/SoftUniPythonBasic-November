number = int(input())

p_one = 0
p_two = 0
p_three = 0
p_four = 0
p_five = 0

for numbers in range(1, number + 1):

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

percentage_p_one = (p_one / number) * 100
percentage_p_two = (p_two / number) * 100
percentage_p_three = (p_three / number) * 100
percentage_p_four = (p_four / number) * 100
percentage_p_five = (p_five / number) * 100

print(f"{percentage_p_one:.2f}%")
print(f"{percentage_p_two:.2f}%")
print(f"{percentage_p_three:.2f}%")
print(f"{percentage_p_four:.2f}%")
print(f"{percentage_p_five:.2f}%")