# Доработать декоратор logger в коде ниже.
# Должен получиться декоратор, который записывает в файл 'main.log' дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась, и возвращаемое значение.
# Функция test_1 в коде ниже также должна отработать без ошибок. import os
from datetime import datetime
import os
def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'date and time: {datetime.now()}\n')
            file.write(f'function name: {old_function.__name__}\n')
            file.write(f'arguments: {args}, {kwargs}\n')
            file.write(f'result: {result}\n')
            file.write('\n')
        return result
    return new_function

def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    @logger
    def get_shop_list_by_dishes(dishes, person_count):
        cook_book = {
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
        list_by_dishes = {}
        if type(dishes) == type([]):
            for i in dishes:
                if i in cook_book:
                    # print(cook_book[i])
                    for j in cook_book[i]:
                        if j['ingredient_name'] in list_by_dishes:
                            list_by_dishes[j['ingredient_name']]['quantity'] += int(j['quantity']) * person_count
                        else:
                            list_by_dishes[j['ingredient_name']] = {'measure': j['measure'],
                                                                    'quantity': int(j['quantity']) * person_count}

    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"

    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()


# Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор,
# который записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась,
# и возвращаемое значение. Путь к файлу должен передаваться в аргументах декоратора. Функция test_2 в
# коде ниже также должна отработать без ошибок. import os
# def logger(path): #@logger(path='путь')
#     def __logger(old_function):
#         def new_function(*args, **kwargs):
#             result = old_function(*args, **kwargs)
#             with open(path, 'a') as file:
#                 file.write(f'date and time: {datetime.now()}\n')
#                 file.write(f'function name: {old_function.__name__}\n')
#                 file.write(f'arguments: {args}, {kwargs}\n')
#                 file.write(f'result: {result}\n')
#                 file.write('\n')
#             return result
#         return new_function
#     return __logger
# def test_2():
#     paths = ('log_1.log', 'log_2.log', 'log_3.log')
#
#     for path in paths:
#         if os.path.exists(path):
#             os.remove(path)
#
#         @logger(path)
#         def hello_world():
#             return 'Hello World'
#
#         @logger(path)
#         def summator(a, b=0):
#             return a + b
#
#         @logger(path)
#         def div(a, b):
#             return a / b
#
#         assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
#         result = summator(2, 2)
#         assert isinstance(result, int), 'Должно вернуться целое число'
#         assert result == 4, '2 + 2 = 4'
#         result = div(6, 2)
#         assert result == 3, '6 / 2 = 3'
#         summator(4.3, b=2.2)
#
#     for path in paths:
#
#         assert os.path.exists(path), f'файл {path} должен существовать'
#
#         with open(path) as log_file:
#             log_file_content = log_file.read()
#
#         assert 'summator' in log_file_content, 'должно записаться имя функции'
#
#         for item in (4.3, 2.2, 6.5):
#             assert str(item) in log_file_content, f'{item} должен быть записан в файл'
# if __name__ == '__main__':
#     test_2()
#
# Применить написанный логгер к приложению из любого предыдущего д/з.