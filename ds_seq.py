shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'Sergei'

# Indexing or 'Subscription' operation
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing a list
print('\n\nItem 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end', shoplist[:])

# Slicing string
print('\n\nCharacters 1 to 3 are', name[1:3])
print('Characters 2 to end are', name[2:])
print('Characters 1 to -1 are', name[1:-1])
print('Characters start to end are', name[:])

# Slicing with differnt step
print('\n')
print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1])
