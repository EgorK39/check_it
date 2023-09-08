""" Вариант 1 """

# list_key = ['hello', '1', '2', '3', '4']
# list_value = ['11', '22', '33', '44', '55']
#
#
# def make_dict(x, y):
#     my_dict = {}
#
#     def func(i):
#         new_dict = {x[i]: y[i]}
#         my_dict.update(new_dict)
#
#     if len(x) > len(y):
#         n = None
#         for i in range(len(x)):
#             if len(y) <= i:
#                 new_dict = {x[i]: n}
#                 my_dict.update(new_dict)
#             else:
#                 func(i)
#     else:
#         for i in range(len(x)):
#             func(i)
#     return my_dict
#
#
# print(make_dict(list_key, list_value))

""" Вариант 2 """
import re


def make_dict():
    my_dict = {}

    def set_key():
        list_key_new = []
        if len(list_key_new) == 0:
            list_key = list(input("Введите ключи: ").split())
            print(f'Введенные ключи: {list_key}')
            if len(list_key) == 0:
                set_key()
                list_key_new.clear()
            else:
                for i in list_key:
                    if not re.findall("\W", i):
                        list_key_new.append(i)
                    else:
                        print(f'Ключи не могут содержать специальные символы. Вы ввели: "{i}".')
                print(f'Список с ключами: {list_key_new}')

        else:
            print(f'Список с ключами: {list_key_new}')
        return list_key_new

    list_key = set_key()

    def set_value():
        list_value_new = []
        if len(list_value_new) == 0:
            list_value = list(input("Введите значения: ").split())
            print(f'Введенные значения: {list_value}')
            if len(list_value) == 0:
                set_value()
                list_value.clear()
            else:
                for i in list_value:
                    list_value_new.append(i)
                print(f'Список со значениями: {list_value_new}')

        else:
            print(f'Список со значениями: {list_value_new}')
        return list_value_new

    list_value = set_value()

    def func(i):
        new_dict = {list_key[i]: list_value[i]}
        my_dict.update(new_dict)

    if len(list_key) > len(list_value):
        n = None
        for i in range(len(list_key)):
            if len(list_value) <= i:
                new_dict = {list_key[i]: n}
                my_dict.update(new_dict)
            else:
                func(i)
    else:
        for i in range(len(list_key)):
            func(i)
    return my_dict


print(make_dict())
