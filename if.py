number = 23
guess = int(input('Enter number:'))

if guess == number:
    # 'If block' starts here
    print('You are right!')
    print('suck it - no prize for you anyway!')
    # Block ends here
elif guess < number:
    # Another block
    print('No, its higher')
    # Block end
else:
    print('No, its smaller number I had in mind')
print('Done')
