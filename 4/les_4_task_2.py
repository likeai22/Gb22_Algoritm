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


def eratosfen(num):
    primes = [2]
    count = 3
    while len(primes) < num:
        for i in primes:
            if count % i == 0:
                break
            if i > count ** (1 / 2):
                primes.append(count)
                break
        count += 1
    return primes[-1]


if __name__ == '__main__':
    prime = 1
    print(timeit.timeit("eratosfen(prime)", setup="from __main__ import eratosfen, prime", number=100))
    # 7.990000085555948e-05
    print(timeit.timeit("eratosfen(prime * 10)", setup="from __main__ import eratosfen, prime", number=100))
    # 0.002133500000127242
    print(timeit.timeit("eratosfen(prime * 100)", setup="from __main__ import eratosfen, prime", number=100))
    # 0.19205160000092292
    print(timeit.timeit("eratosfen(prime * 1000)", setup="from __main__ import eratosfen, prime", number=100))
    # 1.1864953999993304

    cProfile.run('eratosfen(prime * 100)')

    """:cvar
             643 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 les_4_task_2.py:57(eratosfen)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    """

""":cvar
Сложность простого алгоритма O(n^2)
Сложность решета Эратосфена O(n log(log n))
Алгоритм решета Эратосфена эффективен для поиска простого числа с большим порядковым номером
"""