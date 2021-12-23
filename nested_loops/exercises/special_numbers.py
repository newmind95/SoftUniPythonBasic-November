number = int(input())
start = 1111
final = 9999

for num in range(start, final + 1):
    is_special = True

    for digits in str(num):
        digit = int(digits)

        if digit == 0 or number % digit != 0:
            is_special = False
            break
    if is_special:
        print(num, end=' ')
