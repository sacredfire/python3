from collections import OrderedDict

fav_langs = OrderedDict()

# fav_langs = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

fav_langs['jen'] = 'python'
fav_langs['sarah'] = 'c'
fav_langs['edward'] = 'ruby'
fav_langs['phil'] = 'python'

for name, lang in fav_langs.items():
    print("{}'s favourite language is {}.".format(name.title(), lang.title()))
