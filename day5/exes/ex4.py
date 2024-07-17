hours_worked = float(input("Please enter hours worked: "))
hourly_wage = float(input("Please enter hourly wage: "))

total = hourly_wage * hours_worked

if hours_worked > 40:
    total = 40 * hourly_wage + (hours_worked - 40) * hourly_wage * 1.1

print(round(total, 2))
