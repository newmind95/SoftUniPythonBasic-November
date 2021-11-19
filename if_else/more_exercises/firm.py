from math import floor, ceil

hours_need = int(input())  # hours need - integer 0 - 200 000
days_firm_has = int(input())  # days firm has to complete the project - integer [0...20 000]
number_of_employees_work_overtime = int(input())  # integer [0...200]

days_firm_has -= (days_firm_has * (10 / 100))
days_firm_has = days_firm_has * 8

number_of_employees_work_overtime = number_of_employees_work_overtime * (2 * 7)
total_hours = days_firm_has + number_of_employees_work_overtime

diff = abs(total_hours - hours_need)

if total_hours >= hours_need:
    print(f"Yes!{floor(diff)} hours left.")
else:
    print(f"Not enough time!{ceil(diff)} hours needed.")
