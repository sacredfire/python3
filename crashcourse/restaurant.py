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
