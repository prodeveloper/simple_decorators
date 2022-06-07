def take_many_args(a, *args):
    print(a)
    print(args)

def take_many_named_args(a, **kwargs):
    print(a)
    print(kwargs)
if __name__ == '__main__':
    take_many_args(1, 2, 3, 4, 5)
    take_many_named_args(1, b=2, c=3, d=4, e=5)

