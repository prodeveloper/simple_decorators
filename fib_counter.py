from functools import update_wrapper, lru_cache

class Count:
    '''Counts the number of times a function is called'''
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'{self.func.__name__} called {self.count} times')
        return self.func(*args, **kwargs)



@Count
@lru_cache(maxsize=None)
def fib(n):
    '''Generates the nth fibonacci number'''
    if n == 0:
        return 0
    if n==1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(20))