number_of_students_on_exam = int(input())
average_of_grades = 0
low_grade = 0
middle_grade = 0
high_grade = 0
highest_grade = 0

for students in range(1, number_of_students_on_exam + 1):

    grade_of_student = float(input())
    average_of_grades += grade_of_student

    if 2.00 <= grade_of_student <= 2.99:
        low_grade += 1
    elif grade_of_student <= 3.99:
        middle_grade += 1
    elif grade_of_student <= 4.99:
        high_grade += 1
    else:
        highest_grade += 1

percentage_of_highest_grade = (highest_grade * 100) / number_of_students_on_exam
percentage_of_high_grade = (high_grade * 100) / number_of_students_on_exam
percentage_of_middle_grade = (middle_grade * 100) / number_of_students_on_exam
percentage_of_low_grade = (low_grade * 100 ) / number_of_students_on_exam
average_of_grades /= number_of_students_on_exam
print(f"Top students: {percentage_of_highest_grade:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_of_high_grade:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_of_middle_grade:.2f}%")
print(f"Fail: {percentage_of_low_grade:.2f}%")
print(f"Average: {average_of_grades:.2f}")