name_of_student = input()
grades = 1
sum_grades = 0
excluded = 0
is_excluded = False

while grades <= 12:
    grade = float(input()) 

    if grade < 4:
        excluded += 1
        if excluded <= 2:
            is_excluded = True
            break
        continue

    sum_grades += grade
    grades += 1

if is_excluded:
    print('%s has been excluded at %d grade' % (name_of_student, grades))
else:
    average = sum_grades / 12
    print('%s graduated. Average grade: %.2f' % (name_of_student, average))

