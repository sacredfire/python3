def print_max(a, b):
	if a > b:
		print (a, 'is more than', b)
	elif a == b:
		print (a, 'is equal to', b)
	else:
		print (b, 'is more than', a)

# directly pass literal value
print_max(3873773, 994994994)
print_max(44, 44)
print_max(5777, 6)

x = 300
y = 500

# pass variables as arguments
print_max(x, y)
