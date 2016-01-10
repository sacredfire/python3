zoo = ('python', 'cat', 'mouse')

print ('There are {} animals in the zoo.'.format(len(zoo)))

new_zoo = ('tiger', 'pelican', zoo)

print ('Number of cages in the new zoo is {}.'.format(len(new_zoo)))

print ('All animals are {}.'.format(new_zoo))

print ('Animals brought from old zoo are {}.'.format(new_zoo[2]))

print ('Last animal brought from ols zoo is {}.'.format(new_zoo[2][2]))

print ('Number of animals in the new zoo is {}.'
       .format(len(new_zoo) - 1 + len(zoo)))
