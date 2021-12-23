number_of_guests = int(input())
price_per_envelope_for_one_person = float(input())
budget = float(input())
price_of_cake = budget - (budget * 0.90)

if 10 <= number_of_guests <= 15:
    price_per_envelope_for_one_person = price_per_envelope_for_one_person * 0.85
elif 15 <= number_of_guests <= 20:
    price_per_envelope_for_one_person = price_per_envelope_for_one_person * 0.80
elif number_of_guests > 20:
    price_per_envelope_for_one_person = price_per_envelope_for_one_person * 0.75

total_amount_for_party = number_of_guests * price_per_envelope_for_one_person \
                         + price_of_cake

print(price_per_envelope_for_one_person)
print(price_of_cake)
difference = abs(budget - total_amount_for_party)

if budget > total_amount_for_party:
    print('It is party time! %.2f leva left.' % difference)
else:
    print('No party! %.2f leva needed.' % difference)
