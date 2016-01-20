# d = {}
# d['dict1'] = {}
# d['dict1']['innerkey'] = 'value'
# print(d)

person1 = {'name': 'Sergei',
           'surname': 'Kissel',
           'email': 'sergei.kissel@gmail.com',
           'tel': '+380919576297'
           }

person2 = {'name': 'Dmytro',
           'surname': 'Kissel',
           'email': 'exz.mdma@gmail.com',
           'tel': "+16514347900‬"
           }

params = {'me': person1,
          'bro': person2
          }

print(params)

print(params['me'])

print('{} {}'.format(params['me']['name'], params['me']['surname']))

print("My brother's tel num is {}".format(params['bro']['tel']))
