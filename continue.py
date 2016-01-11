while True:
    s = input('Enter something here:')
    if s == 'quit':
        print ('Good bye!')
        break
    if len(s) < 3:
        print ('Too short!')
        continue
    print ('Lenth of the string is {lenth}'.format(lenth=(len(s))))
print ("I\'m done here")
