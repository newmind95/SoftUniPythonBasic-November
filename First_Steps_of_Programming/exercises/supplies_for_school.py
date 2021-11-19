package_pen = 5.80
package_markers = 7.20
detergent = 1.20

number_package_pen = int(input())
number_package_markers = int(input())
liters_of_detergent = int(input())
interest_rate = float(input())

price_package_pen = number_package_pen * package_pen
price_package_markers = number_package_markers * package_markers
price_detergent = liters_of_detergent * detergent

price_all_materials = price_package_pen + price_package_markers + price_detergent
price_discount = price_all_materials - (price_all_materials * interest_rate / 100)


print(price_discount)
