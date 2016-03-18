ab = {'Swaroop': 'swaroop@gmail.com',
      'Larry': 'larry@wall.com',
      'Matrumoto': 'matz@ruby-lang.com',
      'Spammer': 'spammer@spam.com'
      }

print("Swaroop's address is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts total in address book.\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}.'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

print('\nThere are {} contacts total in address book.\n'.format(len(ab)))

for fck, fckrsaddress in ab.items():
    print("Fuck's name is {} and his email is{}\n".format(fck, fckrsaddress))
