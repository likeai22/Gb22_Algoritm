from memory_profiler import profile


@profile
def lesson4_task2_v1(num):
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
    nums = 1000
    lesson4_task2_v1(nums)
    # print(lesson4_task2_v1(nums))

    '''
Line #    Mem usage    Increment   Line Contents
================================================
     4     61.5 MiB     61.5 MiB   @profile
     5                             def lesson4_task2_v1(num):
     6     61.5 MiB      0.0 MiB       primes = [2]
     7     61.5 MiB      0.0 MiB       count = 3
     8     66.7 MiB     -0.9 MiB       while len(primes) < num:
     9     66.7 MiB     -6.4 MiB           for i in primes:
    10     66.7 MiB     -7.4 MiB               if count % i == 0:
    11     66.7 MiB     -1.0 MiB                   break
    12     66.7 MiB     -6.2 MiB               if i > count ** (1 / 2):
    13     66.7 MiB     -0.2 MiB                   primes.append(count)
    14     66.7 MiB     -0.2 MiB                   break
    15     66.7 MiB     -1.8 MiB           count += 1
    16     66.7 MiB      0.0 MiB       return primes[-1]
    '''
