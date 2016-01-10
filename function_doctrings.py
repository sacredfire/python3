def print_max(x, y):
	'''Prints the max out of two numbers.

	The two values must be integers.'''
	x = int(x)
	y = int(y)
	if x < y:
		print (x)
	elif x == y:
		print ('Numbers are equal')
	else:
		print (y)

print_max(3, 6)
print (print_max.__doc__)
