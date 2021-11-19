x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

result = ""

is_valid_first_condition = (x == x1 or x == x2) and (y1 <= y <= y2)
is_valid_second_condition = (y == y1 or y == y2) and (x1 <= x <= x2)

if is_valid_first_condition or is_valid_second_condition:
    result = "Border"
else:
    result = "Inside / Outside"

print(result)