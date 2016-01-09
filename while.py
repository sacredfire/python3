number = 23

while True:
	guess = int(input('Enter number:'))

	if guess == number:
		print ('You are right!')
		print ('..but suck it up - no prize for you anyway!')
		break

	elif guess < number:
		print ('No, it should be higher')

	else:
		print ('No, its smaller number that I had in mind')

print ('The while loop is over')
print ('Done')