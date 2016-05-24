for value in range(1, 5):
    print(value)

print((', ').join(str(value) for value in range(1, 5)))

for value in range(1, 6):
    print(value)

print((', ').join(str(value) for value in range(1, 6)))

numbers = list(range(1, 6))
print(numbers)
print(*numbers)

odd_nums = list(range(1, 11, 2))
print(*odd_nums)

even_nums = list(range(2, 11, 2))
print(*even_nums)

digits = list(range(0, 10))
print(min(digits))
print(max(digits))
print(sum(digits))

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(*squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(*squares)

# This is called list comprehensions
squares = [value**2 for value in range(1, 11)]
print(*squares)
