money_needed_for_charity = int(input())
sum_of_cash_payment = 0
sum_of_card_payment = 0
count_of_sold_cash = 0
count_of_sold_card = 0
counter = 0
total_sum_of_collected_cash = 0
is_money_collected = False

while money_needed_for_charity > 0:
    command = input()
    counter += 1

    if command == 'End':
        is_money_collected = True
        print('Failed to collect required money for charity.')
        break
    
    product = int(command)
    
    if counter % 2 == 0:        # credit card payment
        if product <= 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            sum_of_card_payment += product
            total_sum_of_collected_cash += product
            count_of_sold_card += 1
    else:                       # cash payment
        if product >= 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            sum_of_cash_payment += product
            total_sum_of_collected_cash += product
            count_of_sold_cash += 1

    if total_sum_of_collected_cash >= money_needed_for_charity:
        is_money_collected = True
        average_card_payment = sum_of_card_payment / count_of_sold_card
        average_cash_payment = sum_of_cash_payment / count_of_sold_cash
        print('Average CS: %.2f' % average_cash_payment)
        print('Average CC: %.2f' % average_card_payment)
        break


#if total_sum_of_collected_cash >= money_needed_for_charity:
#        average_card_payment = sum_of_card_payment / 2
#        average_cash_payment = sum_of_cash_payment / 2
#        print('Average CS: %.2f' % average_cash_payment)
#        print('Average CC: %.2f' % average_card_payment)
