"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

numbers_list = [random.randint(-50, 50) for x in range(20)]
# numbers_list = [-2, 1, 2, 2, -30, 0, -2]
total, e_min_cls, e_max_cls = 0, 0, 0

for item in range(len(numbers_list)):
    if numbers_list[item] < numbers_list[e_min_cls]:
        e_min_cls = item
    elif numbers_list[item] > numbers_list[e_max_cls]:
        e_max_cls = item
print(f'list {numbers_list}')
print(f'min {numbers_list[e_min_cls]} index {e_min_cls}\n'
      f'max {numbers_list[e_max_cls]} index {e_max_cls}')

if e_min_cls > e_max_cls:
    for _ in range(e_max_cls + 1, e_min_cls):
        total += numbers_list[_]
else:
    for _ in range(e_min_cls + 1, e_max_cls):
        total += numbers_list[_]

print(f'\nCумма между {numbers_list[e_min_cls]} и {numbers_list[e_max_cls]} = {total}')
