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


# The str class also has a neat method to join the items of a sequence
# with the string acting as a delimiter between each item of the sequence
# and returns a bigger string generated from this.
delimiter = '_*_'
print(delimiter.join(mylist))
