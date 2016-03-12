class Robot:
    """Represents a robot, with a name"""

# A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data"""
        self.name = name
        print('Initizlizing {}'.format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I'm dying."""
        print('{} is being distoyed!'.format(self.name))

        self.name = 'dead robot'

        Robot.population -= 1

        if Robot.population == 0:
            print('No more Robots! {} was the last one.'.format(self.name))
        else:
            print('There are still {:d} robot(s) working'
                  .format(Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        if Robot.population == 0:
            print('No more Robots left!')
        else:
            print('Greetings, my master call my ass {}'.format(self.name))

# Decorators can be imagined to be a shortcut to calling a wrapper function, so
# applying the @classmethod decorator is same as calling:
# how_many = classmethod(how_many)
    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print('We have {:d} robot(s)'.format(cls.population))

    @classmethod
    def kill_em_all(cls):
        """Kills all droid population"""
        print('All Robot(s) are being distoyed!')

        Robot.population = 0


droid1 = Robot("R2-D2")
droid2 = Robot("C3-PO")

droid1.say_hi()
droid2.say_hi()

Robot.how_many()

print('Let\'s kill one')
droid1.die()

print('Let\'s kill the other one')
droid2.die()

print('Let\'s kill \'em all now!')
Robot.kill_em_all()

Robot.how_many()

droid1.say_hi()
droid2.say_hi()

# Here, population belongs to the Robot class and hence is a class variable.
# The name variable belongs to the object (it is assigned using self ) and
# hence is an object variable.

# Thus, we refer to the population class variable as Robot.population and not
# as self.population . We refer to the object variable name using self.name
# notation in the methods of that object.

# Also note that an object variable with the same name as a class variable will
# hide the class variable!

# Instead of Robot.population we could have also used self.__class__.population
# because every object refers to it’s class via the self.__class__ attribute.
