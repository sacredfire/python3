class SchoolMember(object):
    '''Represents any school member'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember: {}'.format(self.name))

    def tell(self):
        '''Tells details'''
        print('Name: {} Age: {}'.format(self.name, self.age), end=' ')
        # 'end' keyword with ' ' parameter has to be used instead of trailing ,


class Teacher(SchoolMember):
    '''Represents teacher'''

    def __init__(self, name, age, salary):
        #
        #
        # This is compatible with Python 2.x
        super(Teacher, self).__init__(name, age)
        #
        #
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))


class Student(SchoolMember):
    '''Represents student'''

    def __init__(self, name, age, grade):
        # Using 'super' method like this is incopatible with Python 2.x!
        super().__init__(name, age)
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

print()
