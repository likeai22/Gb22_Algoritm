from memory_profiler import profile


@profile
def lesson4_task2_v1(number):
    # primes = [2]
    primes = [2, 3]
    i = 1
    while len(primes) < number:
        k = 0
        i += 2
        for j in primes:
            if i % j == 0:
                k = 1
        if k == 0:
            primes.append(i)
    # print(primes)
    return primes[len(primes) - 1]


if __name__ == '__main__':
    nums = 1000
    lesson4_task2_v1(nums)
    # print(lesson4_task2_v1(nums))

    '''
    Line #    Mem usage    Increment   Line Contents
================================================
     4     61.9 MiB     61.9 MiB   @profile
     5                             def lesson4_task2_v1(number):
     6                                 # primes = [2]
     7     61.9 MiB      0.0 MiB       primes = [2, 3]
     8     61.9 MiB      0.0 MiB       i = 3
     9     66.4 MiB    -90.7 MiB       while len(primes) < number:
    10     66.4 MiB    -90.7 MiB           k = 0
    11     66.4 MiB    -90.2 MiB           i += 2
    12     66.4 MiB -68783.1 MiB           for j in primes:
    13     66.4 MiB -68692.8 MiB               if i % j == 0:
    14     66.4 MiB   -165.8 MiB                   k = 1
    15     66.4 MiB    -90.7 MiB           if k == 0:
    16     66.4 MiB    -20.9 MiB               primes.append(i)
    17                                 # print(primes)
    18     66.4 MiB     -0.0 MiB       return primes[len(primes) - 1]
    '''
