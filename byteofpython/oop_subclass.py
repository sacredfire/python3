class SchoolMember:
    '''Represents any school member'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember: {}'.format(self.name))

    def tell(self):
        '''Tells details'''
        print('Name: {} Age: {}'.format(self.name, self.age)),
        # The trailing comma is used not to print new line


class Teacher(SchoolMember):
    '''Represents teacher'''

    def __init__(self, name, age, salary):
        # Init method of the base class is explicitly called using the self
        # variable so that we can initialize the base class part of the object.
        # Python does not automatically call the constructor of the base class
        SchoolMember.__init__(self, name, age)
        # we call methods of the base class by prefixing the class name to the
        # ethod call and then pass in the self variable along with any args.
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))


class Student(SchoolMember):
    '''Represents student'''

    def __init__(self, name, age, grade):
        #
        SchoolMember.__init__(self, name, age)
        self.grade = grade
        print('Initialized Student: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Grade: {:d}'.format(self.grade))

t = Teacher('Mrs. Olivia Stoned', 40, 40000)
s = Student('Michel Foo', 17, 5)

print()

members = [t, s]
for member in members:
    member.tell()
