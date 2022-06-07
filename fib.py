#simple fibonacci implemenmtation
from functools import wraps
def make_posh(func):
    '''Makes a function posh'''
    @wraps(func)
    def posh_func():
        print(f'+------+')
        func()
        print(f'+------+')
    return posh_func
def make_bold_italic(func):
    @wraps(func)
    def wrapper():
        print(f'<b><i>')
        func()
        print(f'</i></b>')
    return wrapper
def bold(func):
    '''Makes a function bold'''
    @wraps(func)
    def wrapper():
        result = f'<b>{func()}</b>'
        return result
    return wrapper
def italic(func):
    '''Makes a function italic'''
    @wraps(func)
    def wrapper():
        result = f'<i>{func()}</i>'
        return result
    return wrapper
def fib(n):
    '''Generates the nth fibonacci number'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
@italic
@bold
def generic_string():
    '''Prints a generic string'''
    return 'Hello World'

print(generic_string())