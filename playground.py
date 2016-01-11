# hello world of strings
message1 = "Hi World!"
message2 = " and go fuck yourself!"
print(message1 + message2)

# format() method with strings
age = 30
name = 'Nick'
name1 = 'Bob'
string = '{} was an asshole when he was {}!'
print (string.format(name, age))
# spacing in chars
string1 = "If you live until {0:5} you'll be like {1}."
print (string1.format(age, name))
# spacing after str but before numbers
string2 = '{0:5} ate {1:.2f} yo sheep!'
print (string2.format(name1, age))
# convert num to str explicitly therefore change spacing to 'after
print (string1.format(str(age), name1))

# table formatting
for i in range(1, 11):
    print('{:2d} {:3d} {:4d}'.format(i, i*i, i*i*i))

# decimal (.) precision of 3 for float '0.333'
print ('{:.3f}'.format(1/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print ('{0:_^20}'.format('Hi!'))
# keyword-based 'Jonny got a gun' and use of escape sequence
print('{name}\'s got a {thing}'.format(name='Jonny', thing='gun'))

# raw string
print(r'Newlines are indicated by \n')
# equivalent to
print('Newlines are indicated by \\n')
