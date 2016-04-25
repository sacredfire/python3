motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles[0] = 'ducati'

print(motorcycles)

motorcycles.append('honda')

print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati')

print(motorcycles)

del motorcycles[0]
del motorcycles[2]

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

popped_motorcylce = motorcycles.pop()

print(motorcycles)

print(popped_motorcylce)

last_owned = motorcycles.pop()

print('{} is the last motorcylce purchased.'.format(last_owned.title()))
