class Bank():
    crisis = False

    def create_atm(self):
        while not self.crisis:
            yield "$100"

x = Bank()

x.create_atm()

# if x.create_atm() == Bank.create_atm(x):
#     print('x.create_atm() == Bank.create_atm(x)')
# else:
#     print('x.create_atm() != Bank.create_atm(x)')
# myobject.method(arg1, arg2) == MyClass.method(myobject, arg1, arg2)


class Restaurant(object):
    bunkrupt = False

    def open_branch(self):
        if not self.bunkrupt:
            print("Branch opened!")

# Create a restaurant
r = Restaurant()

print(r.bunkrupt)
# Same as:
print(Restaurant().bunkrupt)

# Now you can see that self refers to the bound variable or object. In the
# first case it was x because we had assigned the Restaurant class to x whereas
# in the second case it referred to Restaurant().

# Now if we have another Restaurant y, self will know to access the bankrupt
# value of y and not x:
c = Restaurant()

print(c.bunkrupt)

c.open_branch()
