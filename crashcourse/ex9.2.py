class Restaurant(object):
    """Represents restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        print("Opened restaurant {}".format(self.name))

    def describe(self):
        """Tells details"""
        print("This is {} restaurant and it serves {} cuisine".format(
            self.name, self.cuisine))

r = Restaurant("\"Titanic\"", "seafood")
r1 = Restaurant("\"Hot Hell\"", "Mexican")
r2 = Restaurant("\"Cold Day\"", "icecream")

r.describe()
r1.describe()
r2.describe()