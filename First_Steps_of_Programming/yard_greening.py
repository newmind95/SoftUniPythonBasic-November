square_meters = float(input())

one_square_meter = 7.61
discount = 18

price_for_greening = square_meters * one_square_meter
deduct_discount = discount / 100 * price_for_greening

final_price = price_for_greening - deduct_discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {deduct_discount} lv.")
