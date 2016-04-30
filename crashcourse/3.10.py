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
