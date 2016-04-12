class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year, odometer):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.battery = Battery(0.5)

    def get_descriptive_name(self):
        long_name = '\n' + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("{} {} has {} miles on it.".format(
            self.make.title(), self.model.title(), self.odometer))

    def update_odometer(self, mileage):
        print("Updating odometer!")
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        print("Incrementing odometer by {} miles!".format(miles))
        self.odometer += miles

    def fill_gastank(self, gallons):
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


c = Car('audi', 'a5', 2011, 10)

print(c.get_descriptive_name())

c.battery.about_battery()

c.battery.get_range()

c.battery.upgrade_bat()

c.battery.get_range()

c.read_odometer()

c.battery.about_battery()

c.update_odometer(12333.50)

c.read_odometer()

c.update_odometer(12000)

c.read_odometer()

c.increment_odometer(333.5)

c.read_odometer()

# Modifying an Attribute’s Value Directly
c.odometer = 100.7

c.read_odometer()

c.fill_gastank(30)

e = ElecricCar('Tesla', 'model3', 2016, 100)

print(e.get_descriptive_name())

e.read_odometer()

e.battery.about_battery()

e.update_odometer(123.7)

e.read_odometer()

e.fill_gastank(2)

# When we want to describe the battery, we need to work through the car’s
# battery attribute:
e.battery.get_range()

e.battery.upgrade_bat()

e.battery.get_range()

e.battery.about_battery()
