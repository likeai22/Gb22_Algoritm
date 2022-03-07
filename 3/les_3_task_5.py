# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random

numbers_list = [random.randint(-50, 50) for x in range(20)]
index = -1

for item in range(len(numbers_list)):
    if numbers_list[item] < 0 and index == -1:
        index = item
    elif 0 > numbers_list[item] > numbers_list[index]:
        index = item

print(f'list {numbers_list}'
      f'\n{numbers_list[index]}, позиция {index + 1}')
