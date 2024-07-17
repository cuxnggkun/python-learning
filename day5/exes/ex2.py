numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(id(numbers), id(new_numbers))
print(numbers == new_numbers)
print(numbers is new_numbers)

numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))
