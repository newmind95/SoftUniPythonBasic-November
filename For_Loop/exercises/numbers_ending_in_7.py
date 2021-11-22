num = int(input())
max_value = 0

for numbers in range(num):
    current_number = int(input())

    if current_number > max_value:
        max_value = current_number

print(max_value)