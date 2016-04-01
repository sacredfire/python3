class User(object):

    def __init__(self, name1, name2, email):
        self.name1 = name1
        self.name2 = name2
        self.email = email

    def tell(self):
        print("User name is {}\nUser last name is {}\nEmail: {}".format(
            self.name1, self.name2, self.email))

    def greet(self):
        print("Hello {} {}!".format(self.name1, self.name2))

u = User("Sergei", "Kissel", "sergei.kissel@gmail.com")

u.tell()

u.greet()
