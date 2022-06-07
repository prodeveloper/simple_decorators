
from functools import wraps

def munch(start:int, end:int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            replaced_with_x = []
            for index,item in enumerate(result):
                if index >= start and index <end:
                    replaced_with_x.append('x')
                else:
                    replaced_with_x.append(item)
                
            return ''.join(replaced_with_x)

        return wrapper
    return decorator

@munch(1, 6)
def fib():
    return 'Fibonacci'

print (fib())