"""A set of classes used to represent gas and electric cars."""


class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year, odometer):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.battery = Battery(0.5)

    def get_descriptive_name(self):
        """Prints a neatly formatted descriptive name."""
        long_name = '\n' + str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name.title())

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("{} {} has {} miles on it.".format(
            self.make.title(), self.model.title(), self.odometer))

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        print("Updating odometer!")
        if mileage >= self.odometer:
            self.odometer = mileage
            print("{} {} now has {} miles on it."
                  .format(self.make.title(), self.model.title(), self.odometer))
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        print("Incrementing odometer by {} miles!".format(miles))
        self.odometer += miles

    def fill_gastank(self, gallons):
        """Fills tank with max 25 gallons of gasoline"""
        if gallons <= 25:
            self.gallons = gallons
            print("{} {} filled with {:.1f} gallons\n".
                  format(self.make.title(), self.model.title(), self.gallons))
        else:
            self.gallons = 25
            print("Can fill over tank's capacity. {} {} filled with {:.1f} gallons\n".
                  format(self.make.title(), self.model.title(), self.gallons))


class ElecricCar(Car):
    """Child class that represents aspects specific to electric vehicles"""

    def __init__(self, make, model, year, odometer):
        super().__init__(make, model, year, odometer)
        """Initialized attributes of the parent class."""

        self.battery = Battery(70)

    def fill_gastank(self, gallons):
        """Overriding Parent Class method"""
        self.gallons = gallons
        print("Electric cars dont have tank!")


class Battery(object):
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size):
        """Initialize battery attributes"""
        self.battery_size = battery_size

    def about_battery(self):
        """Prints statement about battery size"""
        if self.battery_size <= 1:
            print("This car has conventional battery only.")
        else:
            print("This car's battery size is {} kWh".
                  format(self.battery_size))

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = int(self.battery_size) * 3.23
        print("Range is {} miles.".format(range))

    def upgrade_bat(self):
        print("Installing 85 kWh battery!")
        if self.battery_size <= 1:
            print("Can not fit this big ass battery in here!")
        elif self.battery_size == 85:
            pass
        else:
            self.battery_size = 85
