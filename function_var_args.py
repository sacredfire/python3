def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(20, 1, 2, 3, vegies=50, fruits=100))

print(max(3, 7))


def some():
    # pass statement indicates the empty block of statements
    pass
print(some())

print(total())