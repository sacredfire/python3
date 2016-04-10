class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("\n{} {} has {} miles on it.".format(
            self.make.title(), self.model.title(), self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElecricCar(Car):
    """Child class that represents aspects specific to electric vehicles"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        """
        Initialized attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        self.batery_size = 70

    def about_battery(self):
        """Prints statement about batery size"""
        print("{}'s batery size is {:d} kWh".format(self.model, self.batery_size))


c = Car('audi', 'a5', 2011)

e = ElecricCar('Tesla', 'model3', 2016)

print(c.get_descriptive_name())

print(e.get_descriptive_name())

c.update_odometer(12333.50)

c.read_odometer()

c.update_odometer(12000)

c.read_odometer()

c.increment_odometer(333.5)

c.read_odometer()

# Modifying an Attribute’s Value Directly
c.odometer_reading = 30100

c.read_odometer()

# Calling ElectricCar class instance here
e.update_odometer(123.7)

e.read_odometer()

e.about_battery()
