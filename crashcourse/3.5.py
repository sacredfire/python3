guest_list = ['coco', 'albert', 'david']

for p in guest_list:
    print('{}, you are invited to attend to dinner party!'.format(p.title()))

# or the other way:
print('\n')

print('{}, you are invited to attend to dinner party!'
      .format(guest_list[0].title()))

print('{}, you are invited to attend to dinner party!'
      .format(guest_list[1].title()))

print('{}, you are invited to attend to dinner party!'
      .format(guest_list[2].title()))

# coco cant make it so replace her with Donatella
print('\n')

not_comming = guest_list.pop(0)
print('{} can not attend!'.format(not_comming.title()))

print('These are the only guests left: {}'
      .format(', '.join(str(p) for p in guest_list).title()))

print('\n')

guest_list.append('Donatella')
print('Adding a person..')

print('Now these people are comming: {}'
      .format(', '.join(str(p) for p in guest_list).title()))

print('\n')
for p in guest_list:
    print('{}, you are invited to attend to dinner party!'
          .format(p.title()))
