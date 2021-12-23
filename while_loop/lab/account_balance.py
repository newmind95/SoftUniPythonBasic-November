text = input()
total_balance = 0.0

while text != 'NoMoreMoney':
    amount = float(text)      # contributions to a bank account
    
    if amount < 0:
        print('Invalid operation!')
        break
    
    total_balance += amount
    print('Increase: %.2f' % amount)
    text = input()

print('Total: %.2f' % total_balance)
