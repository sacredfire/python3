trees = ['apple', 'cherry', 'poplar', 'acer', 'oak', 'birch']
print(*trees)

trees.sort()
print(*trees)

trees.reverse()
print(*trees)

trees.reverse()
print(*trees)

trees.reverse()
print(*trees)

tr = sorted(trees)
print(*tr)
print(', '.join(str(t) for t in tr))

print(len(trees))

print(*trees)

trees.reverse()
print(*trees)

trees.insert(4,'walnut')
print(*trees)

trees.remove('walnut')
print(*trees)

latin = 'acer'
trees.remove(latin)
print(*trees)

poped = trees.pop(3)
print(poped)
print(*trees)

poped1 = trees.pop(1)
print(poped1)
print(*trees)

print(', '.join(str(t) for t in trees))
print(len(trees))

poped2 = trees.pop(2)
print(poped2)
