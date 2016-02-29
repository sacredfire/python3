# Here, we define the init method as taking a parameter name (along with the
# usual self ). Here, we just create a new field also called name . Notice
# these are two different variables even though they are both called 'name'.
# There is no problem because the dotted notation self.name means that there
# is something called "name" that is part of the object called "self" and the
# other name is a local variable. Since we explicitly indicate which name we
# are referring to, there is no confusion.

# Most importantly, notice that we do not explicitly call the init method but
# pass the arguments in the parentheses following the class name when creating
# a new instance of the class. This is the special significance of this method.

# Now, we are able to use the self.name field in our methods which is
# demonstrated in the say_hi method.


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Sergei')
p.say_hi()
# Same as:
Person.say_hi(p)

# In the __init__ method, self refers to the newly created object; in other
# class methods, it refers to the instance whose method was called.


# A bit different example
class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print(self.x + ' ' + foo)

a = A()
a.method_a('Sailor!')
# Same as:
A.method_a(a, 'Sailor!')


# Another example showing that the variable set by __init__ is what gets passed
# to instances of the class, not the 'static' variable of the class itself that
# has the same name.
class MyClass(object):
    i = 123

    def __init__(self):
        self.i = 345

a = MyClass()
print(MyClass.i)
print(a.i)
