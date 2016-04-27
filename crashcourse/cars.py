cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print(*cars)
print('{}'.format(', '.join(str(c) for c in cars)))
print(', '.join(str(c) for c in cars))

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(*cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(', '.join(str(c) for c in sorted(cars)))
print('Here is original list again: {}'
      .format(', '.join(str(c) for c in cars)))

# reversing the original list order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(*cars)
cars.reverse()
print(*cars)

print(len(cars))
