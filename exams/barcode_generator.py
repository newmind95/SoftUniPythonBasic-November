start_number = input()
final_number = input()

for num1 in range(int(start_number[0]), int(final_number[0]) + 1):
    for num2 in range(int(start_number[1]), int(final_number[1]) + 1):
        for num3 in range(int(start_number[2]), int(final_number[2]) + 1):
            for num4 in range(int(start_number[3]), int(final_number[3]) + 1):

                if num1 % 2 != 0 and num2 % 2 != 0 \
                   and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
