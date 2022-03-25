from memory_profiler import profile


# @profile
def lesson4_task2_v1(number):
    primes = [2, 3]
    i = 1
    while len(primes) < number:
        k = 0
        i += 2
        v = int(i ** (1 / 2)) + 2
        for j in primes:
            if j > v:
                break
            if i % j == 0:
                k = 1
                break
        if k == 0:
            primes.append(i)
    return primes[len(primes) - 1]


if __name__ == '__main__':
    nums = 999937
    # lesson4_task2_v1(nums)
    print(lesson4_task2_v1(nums))

    '''
        mprof: Sampling memory every 0.1s
    Filename: H:\cloud\_gb\algorithms2\Gb22_Algoritm\6\les_6_task_2_prime_simple_opty3.py
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
     4     61.3 MiB     61.3 MiB   @profile
     5                             def lesson4_task2_v1(number):
     6     61.3 MiB      0.0 MiB       primes = [2, 3]
     7     61.3 MiB      0.0 MiB       i = 1
     8     66.7 MiB     -0.9 MiB       while len(primes) < number:
     9     66.7 MiB     -1.4 MiB           k = 0
    10     66.7 MiB     -1.6 MiB           i += 2
    11     66.7 MiB     -1.6 MiB           v = int(i ** (1 / 2)) + 2
    12     66.7 MiB    -12.1 MiB           for j in primes:
    13     66.7 MiB    -12.1 MiB               if j > v:
    14     66.7 MiB     -0.4 MiB                   break
    15     66.7 MiB    -11.4 MiB               if i % j == 0:
    16     66.7 MiB     -0.9 MiB                   k = 1
    17     66.7 MiB     -1.3 MiB                   break
    18     66.7 MiB     -1.4 MiB           if k == 0:
    19     66.7 MiB     -0.4 MiB               primes.append(i)
    20                                 # print(primes)
    21     66.7 MiB      0.0 MiB       return primes[len(primes) - 1]
    '''
