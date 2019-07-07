def func(self):
    print('func: ', self.__dict__)
    return 'result'


body = dict(__doc__='docstring', __name__='not_A', __module__='modname', __dict__={'a': 1}, f=func)
cls = type('A', (object,), body)

a = cls()
print(a.__doc__)
print(a.__name__)
print(a.__module__)
print(a.f())
