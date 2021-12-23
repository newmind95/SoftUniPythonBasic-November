month_for_average_expense = int(input())
electricity_for_all_months = 0
water_for_all_months = 0
internet_for_all_months = 0
others_for_all_months = 0

for month in range(1, month_for_average_expense + 1):

    electricity = float(input())

    electricity_for_all_months += electricity
    others_for_all_months += (electricity + 20 + 15) * 1.2


water_for_all_months += month_for_average_expense * 20
internet_for_all_months += month_for_average_expense * 15
average_per_month = (electricity_for_all_months + water_for_all_months
                     + internet_for_all_months + others_for_all_months) / month_for_average_expense

print(f"Electricity: {electricity_for_all_months:.2f} lv")
print(f"Water: {water_for_all_months:.2f} lv")
print(f"Internet: {internet_for_all_months:.2f} lv")
print(f"Other: {others_for_all_months:.2f} lv")
print(f"Average: {average_per_month:.2f} lv")