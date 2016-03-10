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

        Robot.population -= 1

        if Robot.population == 0:
            print('No more Robots! {} was the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working'
                  .format(Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print('Greetings, my master call my ass {}'.format(self.name))

        @classmethod
        def how_many(cls):
            """Prints the current population"""
            print('We have {:d} robots'.format(cls.population))

droid1 = Robot("R2-D2")
