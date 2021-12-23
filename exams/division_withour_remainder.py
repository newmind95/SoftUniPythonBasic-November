numbers = int(input())
p1 = 0
p2 = 0
p3 = 0

for number in range(numbers):
    
    current_number = int(input())

    if current_number % 2 == 0:
        p1 += 1

    if current_number % 3 == 0:
        p2 += 1

    if current_number % 4 == 0:
        p3 += 1

percentage_p1 = (p1 / numbers) * 100
percentage_p2 = (p2 / numbers) * 100
percentage_p3 = (p3 / numbers) * 100

print(f'{percentage_p1:.2f}%')
print(f'{percentage_p2:.2f}%')
print(f'{percentage_p3:.2f}%')
