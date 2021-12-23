command = input()

while command != 'End':
    destination = command
    needed_money = float(input())
    counter_saved_money = 0
    while counter_saved_money < needed_money:
        saved_money = float(input())
        counter_saved_money += saved_money

    print('Going to %s' % destination)
    command = input()
