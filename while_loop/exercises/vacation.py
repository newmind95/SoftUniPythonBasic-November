money_need_for_traveling = float(input())
money_on_hand = float(input())
days_to_save = 0
spended_money = 0
saved_money = 0
spending_counter = 0
has_saved_money = True


while money_need_for_traveling > money_on_hand:
    spend_or_saved_money = input()
    amount = float(input())
    days_to_save += 1

    if spend_or_saved_money == 'spend':
        money_on_hand -= amount
        spending_counter += 1
        
        if money_on_hand < 0:
            money_on_hand = 0

        if spending_counter < 5:
            has_saved_money = False
            break
        
    elif spend_or_saved_money == 'save':
        money_on_hand += amount
        spending_counter = 0

if not has_saved_money:
    print("You can't save the money.")
    print('%d' % days_to_save)
else:
    print('You saved the money for %d days.' % days_to_save)
