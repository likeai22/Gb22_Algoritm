# 4.	Определить, какое число в массиве встречается чаще всего.

import random

numbers_list = [-3, 10, -49, 46, -40, -20, 1, 28, 46, -4, 31, -22, 6, 46, 46, 50, 0, -32, 2, 44]
max_cnt, max_num = 0, 0
for i in numbers_list:
    if numbers_list.count(i) > max_cnt:
        max_num = i
        max_cnt = numbers_list.count(i)

print(f'list {numbers_list}\n'
      f'Число {max_num} встречается {max_cnt} раз(а)')
