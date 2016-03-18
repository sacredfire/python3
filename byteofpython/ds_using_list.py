shoplist = ['apple', 'mango', 'potato', 'banana']

print('I have {} items to purchase'.format(len(shoplist)))


def print_shoplist():
    for item in shoplist:
        print(item, end = " ")
        # This 'end = " "' part makes list in one line

print('\nThese items are:')
print_shoplist()

print('\n\nI also need to buy beer..')
shoplist.append('beer')

print('\nMy shoppinglist is now like this:')
print_shoplist()

print('\n\nLet me sort my list now..')
shoplist.sort()

print('\nMy sorted list is:')
print_shoplist()

print('\n\nFirst I\'m gonna buy me {}s'.format(shoplist[0]))
olditem = shoplist[0]
del shoplist[0]
print('\nI bought me {}s.'.format(olditem))

print('\nMy shoppinglist is now like this:')
print_shoplist()
