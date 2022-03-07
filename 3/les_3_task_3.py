# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random

numbers_list = [random.randint(-50, 50) for x in range(20)]

# 1-й вариант
print(f'list {numbers_list}')
e_min_cls = 0
e_max_cls = 0
for item in range(len(numbers_list)):
    if numbers_list[item] < numbers_list[e_min_cls]:
        e_min_cls = item
    elif numbers_list[item] > numbers_list[e_max_cls]:
        e_max_cls = item
print(f'min {numbers_list[e_min_cls]} index {e_min_cls + 1}\n'
      f'max {numbers_list[e_max_cls]} index {e_max_cls + 1}')
pos = numbers_list[e_min_cls]
numbers_list[e_min_cls] = numbers_list[e_max_cls]
numbers_list[e_max_cls] = pos
print(f'new list {numbers_list}\n')

# 2-й вариант
print(f'list {numbers_list}')
e_min, e_max = numbers_list.index(min(numbers_list)), numbers_list.index(max(numbers_list))
numbers_list[e_min], numbers_list[e_max] = numbers_list[e_max], numbers_list[e_min]

print(f'min {min(numbers_list)} index {e_min + 1}\n'
      f'max {max(numbers_list)} index {e_max + 1}\n'
      f'new list {numbers_list}')

