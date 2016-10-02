"""A class that can be used to represent electric cars."""
from car import Car
from battery import Battery


class ElectricCar(Car):
    """Child class that represents aspects specific to electric vehicles"""

    def __init__(self, make, model, year, odometer):
        super().__init__(make, model, year, odometer)
        """Initialized attributes of the parent class."""

        self.battery = Battery(70)

    def fill_gastank(self, gallons):
        """Overriding Parent Class method"""
        self.gallons = gallons
        print("Electric cars dont have tank!")
