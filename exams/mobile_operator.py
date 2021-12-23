contract_term = input()
term_type = input()
added_mobile_internet = input()
number_of_months_for_pay = int(input())

tax = 0
total_price = 0

if contract_term == 'one':
    if term_type == 'Small':
        tax = 9.98
    elif term_type == 'Middle':
        tax = 18.99
    elif term_type == 'Large':
        tax = 25.98
    elif term_type == 'ExtraLarge':
        tax = 35.99
    if added_mobile_internet == 'yes':
        if tax <= 10:
            tax += 5.50
        elif tax <= 30:
            tax += 4.35
        else:
            tax += 3.85

    total_price += tax * number_of_months_for_pay
   
elif contract_term == 'two':
    if term_type == 'Small':
        tax = 8.58
    elif term_type == 'Middle':
        tax = 17.09
    elif term_type == 'Large':
        tax = 23.59
    elif term_type == 'ExtraLarge':
        tax = 31.79

    if added_mobile_internet == 'yes':
        if tax <= 10:
            tax += 5.50
        elif tax <= 30:
            tax += 4.35
        else:
            tax += 3.85
    
    total_price += tax * number_of_months_for_pay

    total_price = total_price - (total_price * (3.75 / 100))

print(f'{total_price:.2f} lv.')


