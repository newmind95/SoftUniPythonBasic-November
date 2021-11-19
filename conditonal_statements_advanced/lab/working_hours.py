working_hours = int(input())
day_of_week = input()

is_valid_working_hours = 10 <= working_hours <= 18

if not is_valid_working_hours or day_of_week == "Sunday":
    print('closed')
else:
    print('open')
