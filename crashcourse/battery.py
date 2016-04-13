"""A class representing automovite batteries."""


class Battery(object):

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
