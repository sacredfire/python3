class Restaurant(object):
    """Represents restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.num_served = 4
        print("Opened restaurant {}".format(self.name))

    def describe(self):
        """Tells all details"""
        print("This is {} restaurant and it serves {} cuisine!".format(
            self.name, self.cuisine))
        print("So far it served {:d} guests.".format(self.num_served))

    def how_many_guests(self):
        """Tells only number of guests served"""
        print(
            "By now, we have served {} guests total!".format(self.num_served))

    def set_guests(self, guests):
        """Sets number of guests that visited"""
        print("..more guests visiting")
        if guests >= self.num_served:
            self.num_served = guests
        else:
            print("Can not be less guests than already served!")

    def add_guests(self, guests):
        """Increases a number of guests by so many."""
        print("...more guests visiting")
        self.num_served += guests

r = Restaurant("Titanic", "seafood")

r.describe()

r.set_guests(67)

r.how_many_guests()

r.add_guests(33)

r.how_many_guests()
