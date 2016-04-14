# d = {}
# d['dict1'] = {}
# d['dict1']['innerkey'] = 'value'
# print(d)

from collections import OrderedDict

person1 = OrderedDict()
person2 = OrderedDict()
params = OrderedDict()

person1['name'] = 'Sergei'
person1['surname'] = 'Kissel'
person1['email'] = 'sergei.kissel@gmail.com'
person1['tel'] = '+380919576297'

person2['name'] = 'Dmytro'
person2['surname'] = 'Kissel'
person2['email'] = 'exz.mdma@gmail.com'
person2['tel'] = '+16514347900'

params['me'] = person1
params['bro'] = person2


print('I am {} {}'.format(params['me']['name'], params['me']['surname']))

print('My brother\'s tel num is {}'.format(params['bro']['tel']))

for value in person1.values():
    print(value, end=' ')

print('\n')

for value in params.values():
    print(value)
