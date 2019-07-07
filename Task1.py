class StaticMethod(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        return self.method


class A:

    def __init__(self):
        print('init')

    @StaticMethod
    def stat():
        return 'static method'


a = A()
print(A.stat())


class ClassMethod(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, owner):
        if owner is None:
            owner = type(instance)

        def new_func(*args):
            return self.method(owner, *args)

        return new_func

class B:
    def __init__(self, attr):
        self.attr = attr

    @ClassMethod
    def cls_method(self, *args, **kwargs):
        return 'cls method'


b = B('spam')
print(b.cls_method())
