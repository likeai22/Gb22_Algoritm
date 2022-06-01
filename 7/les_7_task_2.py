'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import copy
import random


def comparing(i, j):
    print(f'сравниваем {i} и {j}')


def copy_list(array):
    return copy.deepcopy(array)


def merge_sort(array: list) -> list:
    lst = copy_list(array)

    def merge(l_half: list, r_half: list) -> list:

        def _merge():
            while l_half and r_half:
                # comparing(l_half[0], r_half[0])
                yield (l_half if l_half[0] <= r_half[0] else r_half).pop(0)
            yield from l_half
            yield from r_half
        return list(_merge())

    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    # print(lst[:mid], lst[mid:])
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


if __name__ == "__main__":
    array = random.sample(range(0, 50), 10)
    print(array)
    sort_array = merge_sort(array)
    print(sort_array)

    '''
    [48, 2, 18, 41, 46, 39, 15, 10, 32, 38]
    [2, 10, 15, 18, 32, 38, 39, 41, 46, 48]
    '''
