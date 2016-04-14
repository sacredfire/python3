fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']

for name, lang in fav_langs.items():
    print("{}'s favourite language is {}.".format(name.title(), lang.title()))

for name in fav_langs.keys():
    if name in friends:
        print("Hi {}! I see your favourite language is {}".
              format(name.title(), fav_langs[name].title()))
    else:
        pass

for name in sorted(fav_langs.keys()):
    print("{} thanks for taking a poll".format(name.title()))

print("These languages were mentioned:")
for lang in sorted(set(fav_langs.values())):
    print(lang.title())
