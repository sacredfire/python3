class User(object):

    def __init__(self, name1, name2, email):
        self.name1 = name1
        self.name2 = name2
        self.email = email
        self.login_attempts = 0

    def tell(self):
        print("User name is {}\nUser last name is {}\nEmail: {}".format(
            self.name1, self.name2, self.email))
        # print("Login attempts: {:d}".format(self.login_attempts))

    def greet(self):
        print("Hello {} {}!".format(self.name1, self.name2))
#

    def login(self):
        self.login_attempts += 1
        print("Login attempts: {}".format(self.login_attempts))

    def reset(self):
        self.login_attempts = 0
        print("All Reset! Login attempts: {}".format(self.login_attempts))

class Admin(User):

    def __init__(self, name1, name2, email):
        super().__init__(name1, name2, email)
        self.priveleges = {"-can add post", "-can delete post", "-can ban user"}

    def list_preiveleges(self):
        # print(', '.join(str(privelege) for privelege in self.priveleges))
        for privelege in self.priveleges:
            print(privelege)

    def tell(self):
        print("Admin name is {}\nUser last name is {}\nEmail: {}".format(
            self.name1, self.name2, self.email))

a = Admin("Sergei", "Kissel", "sergei.kissel@gmail.com")

a.tell()

a.greet()

a.list_preiveleges()

a.login()

u = User("Dmytro", "Kissel", "exz.mdma@gmail.com")

u.tell()

u.greet()

u.login()

u.login()

u.reset()

u.login()

u.login()

u.login()
