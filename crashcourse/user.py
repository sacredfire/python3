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
