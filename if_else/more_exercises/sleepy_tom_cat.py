count_holiday_days = int(input())

total_hours = 30000
holiday_days = count_holiday_days * 127
work_days = (365 - count_holiday_days) * 63
total = holiday_days + work_days

if total_hours > total:
    total_hours -= total
    total_in_hours = total_hours // 60
    total_in_minutes = total_hours % 60
    print("Tom sleeps well")
    print(f"{total_in_hours} hours and {total_in_minutes} minutes less for play")
else:
    total -= total_hours
    total_in_hours = total // 60
    total_in_minutes = total % 60
    print("Tom will run away")
    print(f"{total_in_hours} hours and {total_in_minutes} minutes more for play")