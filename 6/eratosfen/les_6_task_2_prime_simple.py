from memory_profiler import profile


# @profile
def lesson4_task2_v1(number):
    primes = []
    i = 1
    while len(primes) < number:
        i += 1
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    # print(primes)
    return primes[len(primes) - 1]


if __name__ == '__main__':
    nums = 1000
    # lesson4_task2_v1(nums)
    print(lesson4_task2_v1(nums))

    '''
    mprof: Sampling memory every 0.1s
    running as a Python program...
    Filename: les_6_task_2_prime_simple.py
    
    Line #    Mem usage    Increment   Line Contents
    ================================================
     8     70.8 MiB     70.8 MiB   @profile
     9                             def lesson4_task2_v1(number):
    10     70.8 MiB      0.0 MiB       primes = []
    11     70.8 MiB      0.0 MiB       i = 1
    12     76.7 MiB   -237.4 MiB       while len(primes) < number:
    13     76.7 MiB   -237.4 MiB           i += 1
    14     76.7 MiB -153371.5 MiB           for j in range(2, i):
    15     76.7 MiB -153343.4 MiB               if i % j == 0:
    16     76.7 MiB   -209.8 MiB                   break
    17                                     else:
    18     76.7 MiB    -27.6 MiB               primes.append(i)
    19     76.7 MiB     -0.1 MiB       return primes[len(primes) - 1]
    '''
