from memory_profiler import profile
import random
import cProfile
import timeit


@profile
def lesson3_task9_v1(size):
    mx = [[i * 2 + j * 3 for j in range(size)] for i in range(size)]
    mt = [list(item) for item in zip(*mx)]
    e_min_cls, e_max_cls = 0, 0
    res_lst = []
    for i, line in enumerate(mt):
        for item in range(len(line)):
            if line[item] < line[e_min_cls]:
                e_min_cls = item
        res_lst.append(line[e_min_cls])
    del mt
    for item in range(len(res_lst)):
        if res_lst[item] > res_lst[e_max_cls]:
            e_max_cls = item
    return res_lst[e_max_cls]


if __name__ == '__main__':
    arr_size = 1000
    lesson3_task9_v1(arr_size)

    '''
    Windows10 x64, Python 3.9.12 64 bit
    
    1. Продолжаю исследовать функцию из lesson3 task9.
    В работе представлены 5 файлов с вариантами кода. Заметно, что максимальное использование памяти 
    наблюдается при создании массивов - 38 - 43 MiB и этот результат аналогичен для всех тестируемых функций. 
    В файле les_6_task_1_mtx_for_loop.png (и др. подобных) представлен график времени работы 
    и использования памяти. 
    Наиболее неоптимальное время выполнения наблюдается для функции в les_6_task_1_mtx_for_loop.py,
     объем используемой памяти практически один и тот же для всех задач.
    При работе с массивами, судя по всему, лучше использовать встроенные функции мин/макс python или numpy,
     см. les_6_task_1_mtx_min_max.py, les_6_task_1_mtx_numpy.py и скриншоты к файлам. 
     
     2. Решето Эратосфена.
     
     Решил задачу 4 способами, внешне мало отличающимися, тк постепенно улучшал 
     функцию и добавлял изменения в код следя за выполнением. 
     Здесь les_6_task_2_prime_simple.py и в les_6_task_2_prime_opty.py заметно максимальное
     использование памяти, значение уменьшается при дальнейшей оптимизации. 
     Анализируя отчет memory-profiler, я не заметил моментов очистки памяти, не смотря
     на строки с отрицательными инкрементами практически во всех вариантах кода. 
     Видимо очистка памяти происходит уже после выполнения сборщиками мусора python.
      les_6_task_2_prime_opty[2-4].py    
    '''

    # mx_size = 1
    # print(timeit.timeit("lesson3_task9_v1(mx_size)", setup="from __main__ import lesson3_task9_v1, mx_size",
    #                     number=100))
    # # 0.00040719999999999645
    # print(timeit.timeit("lesson3_task9_v1(mx_size * 10)", setup="from __main__ import lesson3_task9_v1, mx_size",
    #                     number=100))
    # # 0.004060899998876266
    # print(timeit.timeit("lesson3_task9_v1(mx_size * 100)", setup="from __main__ import lesson3_task9_v1, mx_size",
    #                     number=100))
    # # 0.24938709999696584
    # print(timeit.timeit("lesson3_task9_v1(mx_size * 1000)", setup="from __main__ import lesson3_task9_v1, mx_size",
    #                     number=100))
    # # 64.50605910000013
    #
    # cProfile.run('lesson3_task9_v1(mx_size * 1000)')

    """
             2007 function calls in 0.475 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.039    0.039    0.704    0.704 <string>:1(<module>)
            1    0.232    0.232    0.232    0.232 les_6_task_1_mtx_for_loop.py:10(<listcomp>)
            1    0.201    0.201    0.664    0.664 les_6_task_1_mtx_for_loop.py:8(lesson3_task9_v1)
            1    0.003    0.003    0.232    0.232 les_6_task_1_mtx_for_loop.py:9(<listcomp>)
            1    0.000    0.000    0.704    0.704 {built-in method builtins.exec}
         1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
         1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    
    """

    # print(lesson3_task9_v1(arr_size))

    """
    mprof: Sampling memory every 0.1s
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
         7     61.3 MiB     61.3 MiB   @profile
         8                             def lesson3_task9_v1(size):
         9    104.9 MiB     38.9 MiB       mx = [[i * 2 + j * 3 for j in range(size)] for i in range(size)]
        10    114.0 MiB      9.0 MiB       mt = [list(item) for item in zip(*mx)]
        11    114.0 MiB      0.0 MiB       e_min_cls, e_max_cls = 0, 0
        12    114.0 MiB      0.0 MiB       res_lst = []
        13    118.3 MiB    -39.1 MiB       for i, line in enumerate(mt):
        14    118.3 MiB -39097.5 MiB           for item in range(len(line)):
        15    118.3 MiB -39059.7 MiB               if line[item] < line[e_min_cls]:
        16                                             e_min_cls = item
        17    118.3 MiB    -39.1 MiB           res_lst.append(line[e_min_cls])
        18    109.2 MiB     -9.1 MiB       del mt
        19    109.2 MiB      0.0 MiB       for item in range(len(res_lst)):
        20    109.2 MiB      0.0 MiB           if res_lst[item] > res_lst[e_max_cls]:
        21    109.2 MiB      0.0 MiB               e_max_cls = item
        22    109.2 MiB      0.0 MiB       return res_lst[e_max_cls]
    
    """
