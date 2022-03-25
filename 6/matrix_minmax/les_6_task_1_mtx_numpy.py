from memory_profiler import profile
import random
import cProfile
import timeit
import numpy as np


@profile
def lesson3_task9_v3(size):
    mx = [[i * 2 + j * 3 for j in range(size)] for i in range(size)]
    return np.amax(np.amin(mx, axis=0))


if __name__ == '__main__':
    arr_size = 1000
    lesson3_task9_v3(arr_size)

    # mx_size = 1
    # print(timeit.timeit("lesson3_task9_v3(mx_size)", setup="from __main__ import lesson3_task9_v3, mx_size",
    #                     number=100))
    # # 0.00037420000000001896
    # print(timeit.timeit("lesson3_task9_v3(mx_size * 10)", setup="from __main__ import lesson3_task9_v3, mx_size",
    #                     number=100))
    # # 0.007622199998877477
    # print(timeit.timeit("lesson3_task9_v3(mx_size * 100)", setup="from __main__ import lesson3_task9_v3, mx_size",
    #                     number=100))
    # # 0.29667589999735355
    # print(timeit.timeit("lesson3_task9_v3(mx_size * 1000)", setup="from __main__ import lesson3_task9_v3, mx_size",
    #                     number=100))
    # # 33.14450480000232

    # cProfile.run('lesson3_task9_v3(mx_size * 1000)')

    """:cvar
             22 function calls in 0.160 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(amax)
            1    0.000    0.000    0.144    0.144 <__array_function__ internals>:177(amin)
            1    0.012    0.012    0.383    0.383 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2670(_amax_dispatcher)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2675(amax)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2795(_amin_dispatcher)
            1    0.000    0.000    0.144    0.144 fromnumeric.py:2800(amin)
            2    0.000    0.000    0.144    0.072 fromnumeric.py:69(_wrapreduction)
            2    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
            1    0.000    0.000    0.370    0.370 les_6_task_1_mtx_numpy.py:8(lesson3_task9_v3)
            1    0.003    0.003    0.226    0.226 les_6_task_1_mtx_numpy.py:9(<listcomp>)
            1    0.000    0.000    0.383    0.383 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
            2    0.000    0.000    0.144    0.072 {built-in method numpy.core._multiarray_umath.implement_array_function}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            2    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
            2    0.144    0.072    0.144    0.072 {method 'reduce' of 'numpy.ufunc' objects}
    """

    # print(lesson3_task9_v3(arr_size))

    """
    Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
         8     70.6 MiB     70.6 MiB           1   @profile
         9                                         def lesson3_task9_v3(size):
        10    114.7 MiB     43.3 MiB     1003003       mx = [[i * 2 + j * 3 for j in range(size)] for i in range(size)]
        11    114.8 MiB      0.1 MiB           1       return np.amax(np.amin(mx, axis=0))
    """
