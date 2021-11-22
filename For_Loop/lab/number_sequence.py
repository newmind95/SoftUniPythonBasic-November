import sys
number = int(input())
max_value = -sys.maxsize
min_value = sys.maxsize

for numbers in range(0, number):
    current_number = int(input())

    if max_value < current_number:
        max_value = current_number

    if min_value > current_number:
        min_value = current_number

print(f"Max number: {max_value}")
print(f"Min number: {min_value}")
