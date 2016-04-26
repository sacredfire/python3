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
