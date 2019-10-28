def simple_decorator(func_to_decorate):
    def wrapper():
        print('code before original function')
        func_to_decorate()
        print('code after original function')
    return wrapper


def original_function():
    print('i am original')



decorate_original_function = simple_decorator(original_function)
decorate_original_function()

# syntax decorate

@simple_decorator
def reoriginal_function():
    print('i am reorigin')


reoriginal_function()
