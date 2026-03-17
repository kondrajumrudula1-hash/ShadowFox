# 1
friends = ["Asha", "Ravi", "Kiran", "Neha", "Arjun"]

name_length = [(name, len(name)) for name in friends]
print(name_length)

# 2
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transport": 500,
    "Attractions": 300,
    "Misc": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transport": 600,
    "Attractions": 400,
    "Misc": 150
}

# total
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total:", your_total)
print("Partner total:", partner_total)

# who spent more
if your_total > partner_total:
    print("You spent more")
else:
    print("Partner spent more")

# difference
for key in your_expenses:
    diff = abs(your_expenses[key] - partner_expenses[key])
    print(key, "difference:", diff)
