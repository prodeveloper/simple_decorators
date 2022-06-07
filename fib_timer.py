from time import perf_counter
from functools import wraps

def time_function(func):
    '''Times a function'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'{func.__name__} took {end - start} seconds')
        return result
    return wrapper
@time_function
def fib(n):
    '''Generates the nth fibonacci number'''
    if n == 0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(10))