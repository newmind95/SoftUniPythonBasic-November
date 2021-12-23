number_of_eastern_bread = int(input())
number_of_egg_shell = int(input())
kg_of_cookies = int(input())

eastern_bread = 3.20
eggs = 4.35
cookies = 5.40
paint_for_eggs = 0.15

price_easter_bread = number_of_eastern_bread * eastern_bread
price_eggs = number_of_egg_shell * eggs
price_cookies = kg_of_cookies * cookies
price_paint_eggs = number_of_egg_shell * 12 * paint_for_eggs
total_price = price_easter_bread + price_eggs + price_cookies + price_paint_eggs
print('%.2f' % total_price)
