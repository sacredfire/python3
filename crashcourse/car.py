"""A class that can be used to represent a car."""
from battery import Battery


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
