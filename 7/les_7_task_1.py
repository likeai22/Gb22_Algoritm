'''
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
'''
import copy
import random


def comparing(lst, i):
    print(f'сравниваем {lst[i]} и {lst[i + 1]}')


def copy_list(lst):
    return copy.deepcopy(lst)


# a
def bubble_sort(array):
    """пузырёк"""
    lst = copy_list(array)
    length = len(array)
    for i in range(length - 1):
        for j in range(length - 1):
            comparing(lst, j)
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst, bubble_sort.__doc__


def bubble_sort_rec(array):
    """пузырёк с рекурсией"""
    lst = copy_list(array)
    length = len(array)
    swapped = False
    for i in range(length - 1):
        comparing(lst, i)
        if lst[i] < lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            swapped = True
    return [lst, bubble_sort_rec.__doc__] if not swapped else bubble_sort_rec(lst)


# b
def bubble_sort_opt(array):
    """пузырёк улучшенный"""
    lst = copy_list(array)
    length = len(array)
    for i in range(1, length):
        for j in range(0, length - i):
            comparing(lst, j)
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst, bubble_sort_opt.__doc__


if __name__ == "__main__":
    array = random.sample(range(-100, 100), 5)
    print(array)
    # [-60, 97, 98, 35, 31]

    print(*bubble_sort(array), sep=', ')
    '''    
    сравниваем -60 и 97
    сравниваем -60 и 98
    сравниваем -60 и 35
    сравниваем -60 и 31
    сравниваем 97 и 98
    сравниваем 97 и 35
    сравниваем 35 и 31
    сравниваем 31 и -60
    сравниваем 98 и 97
    сравниваем 97 и 35
    сравниваем 35 и 31
    сравниваем 31 и -60
    сравниваем 98 и 97
    сравниваем 97 и 35
    сравниваем 35 и 31
    сравниваем 31 и -60
    '''

    print(*bubble_sort_rec(array), sep=', ')

    print(*bubble_sort_opt(array), sep=', ')
    '''
    сравниваем -60 и 97
    сравниваем -60 и 98
    сравниваем -60 и 35
    сравниваем -60 и 31
    сравниваем 97 и 98
    сравниваем 97 и 35
    сравниваем 35 и 31
    сравниваем 98 и 97
    сравниваем 97 и 35
    сравниваем 98 и 97
    '''

    # 98, 97, 35, 31, -60
