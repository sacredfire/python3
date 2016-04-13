from car import Car
from electric_car import ElectricCar

my_beetle = Car('volswagen', 'beetle', 2015, 9800)

my_tesla = ElectricCar('tesla', 'roadster', '2016', 970)

my_beetle.get_descriptive_name()

my_tesla.get_descriptive_name()

my_tesla.battery.about_battery()
