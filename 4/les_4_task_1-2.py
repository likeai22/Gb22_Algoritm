import cProfile
import timeit
import random


def check_2(size):
    mx = [[random.randint(-50, 50) for i in range(size)] for j in range(size)]
    return max([min(i) for i in [list(item) for item in zip(*mx)]])


if __name__ == '__main__':
    mx_size = 1
    print(timeit.timeit("check_2(mx_size)", setup="from __main__ import check_2, mx_size", number=100))
    # 0.00037420000000001896
    print(timeit.timeit("check_2(mx_size * 10)", setup="from __main__ import check_2, mx_size", number=100))
    # 0.010267199999999976
    print(timeit.timeit("check_2(mx_size * 100)", setup="from __main__ import check_2, mx_size", number=100))
    # 1.1471689999999999
    print(timeit.timeit("check_2(mx_size * 1000)", setup="from __main__ import check_2, mx_size", number=100))
    # 132.44518169999998

    cProfile.run('check_2(mx_size * 100)')

    """
             52776 function calls in 0.024 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.030    0.030 <string>:1(<module>)
            1    0.000    0.000    0.000    0.000 les_4_task_1-2.py:10(<listcomp>)
            1    0.000    0.000    0.029    0.029 les_4_task_1-2.py:8(check_2)
            1    0.000    0.000    0.028    0.028 les_4_task_1-2.py:9(<listcomp>)
        10000    0.007    0.000    0.010    0.000 random.py:237(_randbelow_with_getrandbits)
        10000    0.008    0.000    0.018    0.000 random.py:290(randrange)
        10000    0.004    0.000    0.022    0.000 random.py:334(randint)
            1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
            1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
          100    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        12669    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
    """