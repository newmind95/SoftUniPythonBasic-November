command = input()
sum_of_prime = 0
sum_of_non_prime = 0
is_prime = False

while command != 'stop':

    number = int(command)

    if number < 0:
        print('Number is negative.')
        command = input()
        continue

    is_prime = True
    for digit in range(2, number):
         if number % digit == 0:
                is_prime = False
                break

    if is_prime:
        sum_of_prime += number
    else:
        sum_of_non_prime += number
    
    command = input()

print(f'Sum of all prime numbers is: {sum_of_prime}')
print(f'Sum of all non prime numbers is: {sum_of_non_prime}')
