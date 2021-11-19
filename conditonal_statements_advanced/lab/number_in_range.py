number = int(input())
result = ""
is_valid_number = -100 <= number <= 100 and number != 0

if is_valid_number:
    result = "Yes"
else:
    result = "No"

print(result)