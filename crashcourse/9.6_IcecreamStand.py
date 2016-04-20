class Restaurant(object):
    """Represents restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.num_served = 0
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


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        flavours = ('banana', 'strawberry', 'mango', 'apple', 'caramel')
        self.flavours = flavours

    def list_flavours(self):
        print("Availbale flavours are:")
        # for flavour in self.flavours:
        #     print(flavour)

        print(', '.join(str(flavour) for flavour in self.flavours))

i = IceCreamStand("Snow white", "desets")
i.describe()
i.list_flavours()
