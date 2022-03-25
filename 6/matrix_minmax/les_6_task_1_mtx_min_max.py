from memory_profiler import profile
import random
import cProfile
import timeit


@profile
def lesson3_task9_v2(size):
    mx = [[i * 2 + j * 3 for j in range(size)] for i in range(size)]
    return max([min(i) for i in [list(item) for item in zip(*mx)]])


if __name__ == '__main__':
    arr_size = 1000
    lesson3_task9_v2(arr_size)

    # mx_size = 1
    # print(timeit.timeit("lesson3_task9_v2(mx_size)", setup="from __main__ import lesson3_task9_v2, mx_size",
    #                     number=100))
    # # 0.00037420000000001896
    # print(timeit.timeit("lesson3_task9_v2(mx_size * 10)", setup="from __main__ import lesson3_task9_v2, mx_size",
    #                     number=100))
    # # 003008100000442937
    # print(timeit.timeit("lesson3_task9_v2(mx_size * 100)", setup="from __main__ import lesson3_task9_v2, mx_size",
    #                     number=100))
    # # 0.18512170000030892
    # print(timeit.timeit("lesson3_task9_v2(mx_size * 1000)", setup="from __main__ import lesson3_task9_v2, mx_size",
    #                     number=100))
    # # 47.396435499998915

    # cProfile.run('lesson3_task9_v2(mx_size * 1000)')

    """:cvar
             1007 function calls in 0.243 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.013    0.013    0.483    0.483 <string>:1(<module>)
            1    0.001    0.001    0.470    0.470 les_6_task_1_mtx_min_max.py:7(lesson3_task9_v2)
            1    0.003    0.003    0.224    0.224 les_6_task_1_mtx_min_max.py:8(<listcomp>)
            1    0.186    0.186    0.186    0.186 les_6_task_1_mtx_min_max.py:9(<listcomp>)
            1    0.000    0.000    0.483    0.483 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
         1000    0.041    0.000    0.041    0.000 {built-in method builtins.min}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """

    # print(lesson3_task9_v2(arr_size))

    """:cvar
    mprof: Sampling memory every 0.1s
    running as a Python program...
    Filename: les_6_task_1_mtx_min_max.py
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
         7     61.6 MiB     61.6 MiB   @profile
         8                             def lesson3_task9_v2(size):
         9    105.1 MiB     40.8 MiB       mx = [[i * 2 + j * 3 for j in range(size)] for i in range(size)]
        10    114.2 MiB      0.2 MiB       return max([min(i) for i in [list(item) for item in zip(*mx)]])    
    """
