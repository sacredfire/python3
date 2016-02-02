print('Simple assignment where two names point to same object:')
shoplist = ['apple', 'mango', 'carrot', 'banana']
print(shoplist)

mylist = shoplist
print(mylist)

del shoplist[0]
print('My list is now', mylist)
print('Shop list is now', shoplist)

print('\nCopy by making a full slice:')
mylist = shoplist[:]

del mylist[0]
print('My list is now', mylist)
print('Shop list is now', shoplist)
# Note that two lists are different
