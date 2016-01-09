number = 23

while True:
    guess = int(input('Enter any number:'))

    if guess == number:
        print ('You guessed correct!')
        break
    
    elif guess < number:
        print ('No, try bigger number')
    
    else:
    	print ('No, try smaller number')

print ('The end!')