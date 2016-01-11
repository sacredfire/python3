def maximum(x, y):
    if x > y:
        return x
    elif y == x:
        return 'Numbers are equal'
    else:
        return y

print (maximum(100, 500))
print (maximum(600, 600))

print (max(50, 50))
print (max(50, 51))
