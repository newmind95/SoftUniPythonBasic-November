walks = 10000
sum_of_steps = 0
has_reached_goal = False

while sum_of_steps < walks and not has_reached_goal:

    command = input()

    if command == 'Going home':
        command = input()
        has_reached_goal = True
        
    current_steps = int(command)
    sum_of_steps += current_steps

difference = abs(sum_of_steps - walks)

if sum_of_steps >= walks:
    print('Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')
