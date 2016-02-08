
while True:
    name = input(str('What\'s your name?\n'))

    if name == 'quit':
        print('Bye!')
        break

    if name.startswith('Ser'):
        print("Yes, the string starts with 'Ser'")
    else:
        print("No string does not start with 'Str'")

    if 'i' in name:
        print("Yes, there is 'i' in name")
    else:
        print("No there is no 'i' in name")

# The find method is used to locate the position of the given substring
# within the string; find returns -1 if it is unsuccessful in finding the
# substring.
    if name.find('fuck') != -1:
        print("Yes, the string has some 'fuck' in it")
    if name.find('bitch') != -1:
        print("'Bitch' string found!")
    else:
        print("No bitches found no fucks given")
