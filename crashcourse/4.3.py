print(', '.join(str(number) for number in range(1, 21)))

grand = [value for value in range(1, 1001)]
print(*grand)

mil = list(range(1, 1000001))
print(min(mil))
print(max(mil))
print(sum(mil))

odd_nums = [value for value in range(1, 21, 2)]
print(*odd_nums)

odd_nums = list(range(1, 21, 2))
print(*odd_nums)

print(' '.join(str(value) for value in range(1, 21, 2)))

times_3 = [value * 3 for value in range(1, 31)]
print(*times_3)

print(' '.join(str(value * 3) for value in range(1, 31)))

cubes = [value**3 for value in range(1, 11)]
print(*cubes)

print(' '.join(str(value**3) for value in range(1, 11)))

cubes_alt = []
for value in range(1, 11):
    cubes_alt.append(value**3)
print(*cubes_alt)

cubes_alt = []
for value in range(1, 11):
    cubes_alt.append(value**3)
print(*cubes_alt)
