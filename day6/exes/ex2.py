employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

total = 0

for employee in employees:
    total += employee[2]

average_wage = total / len(employees)

for employee in employees:
    if employee[2] > average_wage:
        print(f"{employee[0]} earns more than average.")
