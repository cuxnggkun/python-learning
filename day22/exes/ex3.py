import itertools as it

employees = it.cycle(["Cuong", "Hoa", "Hung"])
weeks = it.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

for _ in range(1, 31):
    print(f"{next(employees)} - {next(weeks)}")
