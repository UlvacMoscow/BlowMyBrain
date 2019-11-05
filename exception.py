# try:
    # область действия обработчика
# except Exception1:
    # обработчик исключений1
# except Exception2:
    # обработчик исключений2
# except Exception3:
    # обработчик исключений3
# else:
    # код который выполняется если никакого исключения не возникло
# finally:
    # код который выполняеться в любом случае

# raise принудительно вызвать исключение нужно исключение и сам объект для исключения

try:
    f = open('simple.txt', 'r') # run2
    # f = open('simple.txt', 'w') # run1
    f.write('Test test test')
except IOError:
    print('Error: could not find file to read data!')
# else:
#     print('success')
#     f.close()
finally:
    print('i always work')

# raise NameError('I am object of string')

# создаем свой класс исключение он должен быть унаследован от класса Exception явно или нет


class MyError(Exception):
    def __init__(self, value):
        self.value = value

try:
    raise MyError(5*5)
except MyError as e:
    print('My Exception with value: ', e.value)
