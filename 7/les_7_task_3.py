'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
'''

import random


def quick_select(array, med):
    pivot = random.choice(array)
    array1, array2 = [], []

    for item in array:
        if item < pivot:
            array1.append(item)
        elif item > pivot:
            array2.append(item)
        else:
            pass

    if med <= len(array1):
        return quick_select(array1, med)
    elif med > len(array) - len(array2):
        return quick_select(array2, med - (len(array) - len(array2)))
    else:
        return pivot


num = random.randint(0, 10)
mass = random.sample(range(100), 2 * num + 1)
med_idx = len(mass) // 2 + 1
print("\nИсходный список: %s\nМедиана: %d" % (mass, quick_select(mass, med_idx)))
