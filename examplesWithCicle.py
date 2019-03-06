from collections import defaultdict, Counter
from itertools import chain
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
list_name_students = []
for student in students:
  # print(student.get(*student.keys()))
    list_name_students.append(student.get(*student.keys()))

# print(Counter(list_name_students))

# my_dict = defaultdict(int)
# for el in students:
#     print(el.items())
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
list_name_students_2 = []
for student in students:
    # print(*student.keys())
    # print(student.get(*student.keys()))
    list_name_students_2.append(student.get(*student.keys()))

# print(Counter(list_name_students_2).most_common(1))
# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]

task3 = []
temp = school_students
for index, class_scl in enumerate(school_students, 1):
    # print(f"Самое частое имя в классе {index}", end='')
    # print(' pop ', class_scl[0].pop('first_name'))
    # print(class_scl)
    for elem in class_scl:
        # print('elem ', elem)
        task3.append(elem.pop('first_name'))
        print(f"Самое частое имя в классе {index}:", end='')
        print(*Counter(task3).most_common(1))
        task3 = []
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
a = (list(chain.from_iterable(d.values() for d in class_name['students'])) for class_name in school)

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

dict_1 = defaultdict(int)
for el in a:
    for key in el:
        if is_male[key]:
            dict_1['girls'] += el[key]
            print(11)
        else:
            print(22)
            dict_1['boys'] += el[key]

print(dict_1)


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
