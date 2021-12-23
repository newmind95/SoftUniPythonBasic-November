failed_grades = int(input())
solved_problems_count = 0
last_problem = ''
poor_grades = 0
sum_of_grades = 0
is_failed = True

while poor_grades < failed_grades:
    name_of_exercise = input()

    if name_of_exercise == 'Enough':
        is_failed = False
        break

    grade = int(input())
    if  grade <= 4:
        poor_grades += 1

    sum_of_grades += grade
    solved_problems_count += 1
    last_problem = name_of_exercise

if is_failed:
    print('You need a break, %d poor grades.' % poor_grades)
else:
    average_score = sum_of_grades / solved_problems_count
    print('Average score: %.2f' % average_score)
    print('Number of problems: %d' % solved_problems_count)
    print('Last problem: %s' % last_problem)
