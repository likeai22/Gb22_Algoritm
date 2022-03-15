import cProfile
import timeit
import numpy as np


def check_3(num):
    mx = np.random.randint(-50, 50, size=(num, num))
    return np.amax(np.amin(mx, axis=0))


if __name__ == '__main__':
    mx_size = 1
    print(timeit.timeit("check_3(mx_size)", setup="from __main__ import check_3, mx_size", number=100))
    # 0.006573200000000001
    print(timeit.timeit("check_3(mx_size * 10)", setup="from __main__ import check_3, mx_size", number=100))
    # 0.006516499999999981
    print(timeit.timeit("check_3(mx_size * 100)", setup="from __main__ import check_3, mx_size", number=100))
    # 0.016681200000000007
    print(timeit.timeit("check_3(mx_size * 1000)", setup="from __main__ import check_3, mx_size", number=100))
    # 1.1692671
    print(timeit.timeit("check_3(mx_size * 10000)", setup="from __main__ import check_3, mx_size", number=100))
    # 114.21665320000001

    cProfile.run('check_3(mx_size * 100)')
    """
             30 function calls in 0.001 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(amax)
            1    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(amin)
            1    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(prod)
            1    0.000    0.000    0.000    0.000 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2670(_amax_dispatcher)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2675(amax)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2795(_amin_dispatcher)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2800(amin)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2965(_prod_dispatcher)
            1    0.000    0.000    0.000    0.000 fromnumeric.py:2970(prod)
            3    0.000    0.000    0.000    0.000 fromnumeric.py:69(_wrapreduction)
            3    0.000    0.000    0.000    0.000 fromnumeric.py:70(<dictcomp>)
            1    0.000    0.000    0.000    0.000 les_4_task_1-3.py:13(check_3)
            1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
            3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
            3    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
            1    0.000    0.000    0.000    0.000 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
            3    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
    """
