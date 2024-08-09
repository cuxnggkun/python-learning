students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 92},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

valedictorian = max(students, key=lambda student: student["grade_average"])
print(valedictorian)
