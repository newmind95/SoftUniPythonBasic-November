flag = False
symbols = '%!^`(){}"\'\+,-/'
secret_command = ''

while True:

    letter = input()

    if letter == 'End':
        flag = True
        break
    
#    if letter == symbols:
#        continue
#    else:
#        secret_command += letter

    if letter == 'c' or letter == 'o' or letter == 'n':
        secret_command += 'o'
        continue
    else:
        secret_command += letter
    
    
print(secret_command + " ")
        
