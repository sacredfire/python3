fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']

to_poll = ['edward', 'phil', 'sarah', 'nick', 'steve', 'jen']

print("These people already responded:")
for name in fav_langs.keys():
    if name in to_poll:
        print(name.title())

print("These are still to be polled:")
for name in to_poll:
    if name not in fav_langs.keys():
        print(name.title())
