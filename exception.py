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

try:
    f = open('simple.txt', 'w')
    f.write('Test test test')
except IOError:
    print('Error: could not find file to read data!')
else:
    print('success')
    f.close()
