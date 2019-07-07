import re


class EmailDescriptor:
    def __init__(self, email, name='email'):
        self.mail = email
        self.name = name

    def __get__(self, instance, owner):
        print('Get', self.name, self.mail)
        return self.mail

    def __set__(self, instance, value):
        my_pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
        pattern = re.compile(my_pattern)
        print('Try to set', self.name, value)
        if not re.match(pattern, value):
            print('You failed to set email {}'.format(value))
        else:
            self.mail = value
            print('You set email {} successful'.format(value))


class MyClass:
    email = EmailDescriptor('', 'email')


my_class = MyClass()
my_class.email
my_class.email = "validemail@gmail.com"
my_class.email
my_class.email = "novalidemail"
my_class.email
