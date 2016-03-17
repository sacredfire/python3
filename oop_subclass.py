class SchoolMember:
    '''Represents any school member'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember:'.format(self.name))

    def tell(self):
        '''Tesubllls details'''
        print