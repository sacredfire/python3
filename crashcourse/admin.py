from user import User


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
