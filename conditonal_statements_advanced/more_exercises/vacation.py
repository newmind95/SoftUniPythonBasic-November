budget = float(input())
season = input()

if budget <= 1000:
    if season == "Summer":
        budget = budget * (65 / 100)
        print(f"Alaska - Camp - {budget:.2f}")
    elif season == "Winter":
        budget = budget * (45 / 100)
        print(f"Morocco - Camp - {budget:.2f}")
elif 1000 < budget <= 3000:
    if season == "Summer":
        budget = budget * (80 / 100)
        print(f"Alaska - Hut - {budget:.2f}")
    elif season == "Winter":
        budget = budget * (60 / 100)
        print(f"Morocco - Hut - {budget:.2f}")
else:
    budget = budget * (90 / 100)
    if season == "Summer":
        print(f"Alaska - Hotel - {budget:.2f}")
    elif season == "Winter":
        print(f"Morocco - Hotel - {budget:.2f}")