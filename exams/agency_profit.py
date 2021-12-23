name_of_airline = input()
number_of_tickets_for_adults = int(input())
number_of_tickets_for_children = int(input())
net_worth_ticket_for_adults = float(input())
tax = float(input())

total_price_children_ticket = net_worth_ticket_for_adults - (net_worth_ticket_for_adults * (70 / 100))
price_tax_for_adults = net_worth_ticket_for_adults + tax
price_tax_for_children = total_price_children_ticket + tax
total_price_for_tickets = (number_of_tickets_for_children * price_tax_for_children) \
    + (number_of_tickets_for_adults * price_tax_for_adults)
profit = total_price_for_tickets * (20 / 100)

print(f"The profit of your agency from {name_of_airline}"
      f" tickets is {profit:.2f} lv.")