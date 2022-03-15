"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import cProfile
import timeit


# Вариант 1 (простой)
def simple(number):  # Где n, это номер искомого простого числа.
    primes = []
    i = 1

    while len(primes) < number:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)

    return primes[len(primes) - 1]


if __name__ == '__main__':
    prime = 1
    print(timeit.timeit("simple(prime)", setup="from __main__ import simple, prime", number=100))
    # 6.320000000001325e-05
    print(timeit.timeit("simple(prime * 10)", setup="from __main__ import simple, prime", number=100))
    # 0.0015489999999999948
    print(timeit.timeit("simple(prime * 100)", setup="from __main__ import simple, prime", number=100))
    # 0.14265540000000002
    print(timeit.timeit("simple(prime * 1000)", setup="from __main__ import simple, prime", number=100))
    # 22.7112686

    cProfile.run('simple(prime * 100)')

    """
             646 function calls in 0.002 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.001    0.001 <string>:1(<module>)
            1    0.001    0.001    0.001    0.001 les_4_task_2.py:13(simple)
            1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
          542    0.000    0.000    0.000    0.000 {built-in method builtins.len}
          100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
            1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """

    # Вариант 2 (решето Эратосфена)

