import car
import electric_car

# Import an entire module and then access the classes you need
# using dot notation.
my_beetle = car.Car('volswagen', 'beetle', 2015, 9800)

my_tesla = electric_car.ElectricCar('tesla', 'roadster', '2016', 970)

my_beetle.get_descriptive_name()

my_tesla.get_descriptive_name()

my_tesla.battery.about_battery()
