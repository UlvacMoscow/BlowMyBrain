def decorate_args(func):
    def wrapper(arg1, arg2):
        print(' i am get ', arg1, arg2)
        func(arg1, arg2)
    return wrapper


@decorate_args
def print_full_name(first_name, second_name):
    print('my name is ',first_name, second_name)


print_full_name('sen', 'senov')
