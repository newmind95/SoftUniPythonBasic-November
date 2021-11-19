number_of_juniors_group = int(input())
number_of_seniors_group = int(input())
trace_type = input()
donation_amount = 0
total_price = 0

if trace_type == "trail":
    tax_juniors = 5.50
    tax_seniors = 7
    total_price = (number_of_juniors_group * tax_juniors) + (number_of_seniors_group * tax_seniors)
    costs = total_price * (5 / 100)
    left = total_price - costs
    donation_amount = left
elif trace_type == "cross-country":
    if number_of_seniors_group + number_of_juniors_group >= 50:
        tax_juniors = 8
        tax_seniors = 9.50
        total_price = (number_of_juniors_group * tax_juniors + number_of_seniors_group * tax_seniors) \
            * 0.75 * 0.95
        donation_amount = total_price
    else:
        tax_juniors = 8
        tax_seniors = 9.50
        total_price = (number_of_juniors_group * tax_juniors) + (number_of_seniors_group * tax_seniors)
        costs = total_price * (5 / 100)
        left = total_price - costs
        donation_amount = left
elif trace_type == "downhill":
    tax_juniors = 12.25
    tax_seniors = 13.75
    total_price = (number_of_juniors_group * tax_juniors + number_of_seniors_group * tax_seniors)
    costs = total_price * (5 / 100)
    left = total_price - costs
    donation_amount = left
elif trace_type == "road":
    tax_juniors = 20
    tax_seniors = 21.50
    total_price = (number_of_juniors_group * tax_juniors + number_of_seniors_group * tax_seniors)
    costs = total_price * (5 / 100)
    left = total_price - costs
    donation_amount = left

print(f"{donation_amount:.2f}")