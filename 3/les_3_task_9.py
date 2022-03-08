# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[15, 4, 55],
          [25, 6, 8],
          [12, 11, 1]]

matrix_t = [list(item) for item in zip(*matrix)]
e_min_cls, e_max_cls = 0, 0

res_lst = []
for i, line in enumerate(matrix_t):
    for item in range(len(line)):
        if line[item] < line[e_min_cls]:
            e_min_cls = item
    res_lst.append(line[e_min_cls])
for item in range(len(res_lst)):
    if res_lst[item] > res_lst[e_max_cls]:
        e_max_cls = item

print(res_lst[e_max_cls])
