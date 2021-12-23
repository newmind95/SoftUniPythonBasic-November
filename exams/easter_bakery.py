price_flour_one_kg = float(input())
kg_of_flour = float(input())
kg_of_sugar = float(input())
number_of_egg_shell = int(input())
package_of_yeast = int(input())

price_of_sugar = price_flour_one_kg * 0.75
price_of_egg_shell = price_flour_one_kg + (price_flour_one_kg * (10 / 100))
price_of_yeast = price_of_sugar * 0.2
amount_for_flour = price_flour_one_kg * kg_of_flour
amount_for_sugar = price_of_sugar * kg_of_sugar
amount_for_eggs = price_of_egg_shell * number_of_egg_shell
amount_for_yeast = price_of_yeast * package_of_yeast

total_amount = amount_for_flour + amount_for_sugar + \
    amount_for_eggs + amount_for_yeast
print('%.2f' % total_amount)
