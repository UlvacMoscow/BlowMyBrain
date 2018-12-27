# Задание с сайта Chekio island o'Reilly task cipher map



def recall_password(case, table):
    """ всего 16 итерация """
    word = ''
    for index in range(4):
        for index in range(4):
            word += compiled_word(case, table, index)
        case = transform_table(case)
    return word


def compiled_word(case, table, index):
    """ здесь мы выбираем нужные нам буквы по нашему отпечатку плиты
        главный недостаток что первые две итерации отличаються от дву последних по исполнению
    """
    word = ''
    if case[index].count('X') == 1:
        word += add_cesar(case, table, index)
    elif case[index].count('X') == 2:
        word += add_cesar(case, table, index)
        temp = table[index][::-1]
        temp1 = case[index][::-1]
        word += temp[temp1.index('X')]
    elif case[index].count('X') == 3:
        point = case[index].index('.')
        temp2 = list(table[index])
        temp2.pop(point)
        word += ''.join(temp2)
    elif case[index].count('X') == 4:
        word += table[index]
    return word


def add_cesar(case, table, index):
    """ вырезаю букву по таблицы где расположен X """
    return table[index][case[index].index('X')]


def transform_table(case):
    """крутим нашу плиту с шифром на 90 градусов"""
    return tuple(zip(*case[::-1]))


print(recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),

    ('itdf',
     'gdce',
     'aton',
     'qrdi')))
