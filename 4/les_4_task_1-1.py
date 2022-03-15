"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# 9 задача дз3
import cProfile
import timeit
import random


def check_1(size):
    mx = [[random.randint(-50, 50) for i in range(size)] for j in range(size)]
    mt = [list(item) for item in zip(*mx)]
    e_min_cls, e_max_cls = 0, 0
    res_lst = []
    for i, line in enumerate(mt):
        for item in range(len(line)):
            if line[item] < line[e_min_cls]:
                e_min_cls = item
        res_lst.append(line[e_min_cls])
    for item in range(len(res_lst)):
        if res_lst[item] > res_lst[e_max_cls]:
            e_max_cls = item
    return res_lst[e_max_cls]


if __name__ == '__main__':
    mx_size = 1
    print(timeit.timeit("check_1(mx_size)", setup="from __main__ import check_1, mx_size", number=100))
    # 0.00040719999999999645
    print(timeit.timeit("check_1(mx_size * 10)", setup="from __main__ import check_1, mx_size", number=100))
    # 0.010771400000000014
    print(timeit.timeit("check_1(mx_size * 100)", setup="from __main__ import check_1, mx_size", number=100))
    # 1.1581393
    print(timeit.timeit("check_1(mx_size * 1000)", setup="from __main__ import check_1, mx_size", number=100))
    # 114.21665320000001

    cProfile.run('check_1(mx_size * 100)')
    """
          52897 function calls in 0.023 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.001    0.001    0.028    0.028 <string>:1(<module>)
            1    0.001    0.001    0.027    0.027 les_4_task_1-1.py:13(check_1)
            1    0.000    0.000    0.025    0.025 les_4_task_1-1.py:14(<listcomp>)
            1    0.000    0.000    0.000    0.000 les_4_task_1-1.py:15(<listcomp>)
        10000    0.006    0.000    0.009    0.000 random.py:237(_randbelow_with_getrandbits)
        10000    0.008    0.000    0.016    0.000 random.py:290(randrange)
        10000    0.004    0.000    0.020    0.000 random.py:334(randint)
            1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
          101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
          100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        12690    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
    """

    """
    Сложность алгоритма O(n^2).
    52897 вызовов функции и 52776 в les_4_task_2.py. Из них больше 40000 пришлось на работу random.
    Поиск минимума/максммума в массивах с помощью хвостовой рекурсией дает еще более медленный результат,
    в домашнем задании его нет, тк не удалось исправить ошибку exit code -1073741571, setrecursionlimit
      не помог. Оставил на потом.
    С numpy (les_4_task_3.py) в 100 уменьшилось время работы и более, чем в 1000 раз сократилось 
    количество вызовов
    """
