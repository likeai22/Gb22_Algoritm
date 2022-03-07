"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

import random

numbers_list = [random.randint(-50, 50) for x in range(20)]

value_1, value_2 = numbers_list[0], None
for item in numbers_list[1:]:
    if item < value_1:
        value_1, value_2 = item, value_1
    elif value_2 is None or item < value_2:
        value_2 = item
print(f'list {numbers_list}')
print(f'min1 {value_1}\n'
      f'min2 {value_2}')
