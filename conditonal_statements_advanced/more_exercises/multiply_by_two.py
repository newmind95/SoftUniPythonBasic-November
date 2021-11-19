num = float(input())
result = 0

while num >= 0:
    result = num * 2
    print(f"Result {result:.2f}")
    num = float(input())

    if num < 0:
        print('Negative number!')
        break