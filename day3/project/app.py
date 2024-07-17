name = input("Please enter your name: ").strip().title()
hourly_wage = float(input("Please enter your hourly wage: "))
hourly_worked = float(input("Please enter hours the employee worked this week: "))

total_earnings = hourly_wage * hourly_worked
total_earnings_rounds = round(total_earnings, 2)
total_earnings_format = format(total_earnings, ".2f")

print(f"{name} earned ${total_earnings:.2f} this week.")
print(f"{name} earned ${total_earnings_rounds} this week.")
print(f"{name} earned ${total_earnings_format} this week.")
