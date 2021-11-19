fruit_or_vegetable = input()
fruit_or_vegetable_type = ""

is_valid_fruit = fruit_or_vegetable == "banana" or fruit_or_vegetable == "apple" \
        or fruit_or_vegetable == "kiwi" or fruit_or_vegetable == "cherry" \
        or fruit_or_vegetable == "lemon" or fruit_or_vegetable == "grapes"

is_valid_vegetable = fruit_or_vegetable == "tomato" or fruit_or_vegetable == "cucumber"\
        or fruit_or_vegetable == "pepper" or fruit_or_vegetable == "carrot"

if is_valid_fruit:
    fruit_or_vegetable_type = "fruit"
elif is_valid_vegetable:
    fruit_or_vegetable_type = "vegetable"
else:
    fruit_or_vegetable_type = "unknown"

print(fruit_or_vegetable_type)