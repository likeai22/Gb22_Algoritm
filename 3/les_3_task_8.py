"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []
for i in range(4):
    for j in range(1):
        row = input().split()
        matrix_row = list(map(int, row))
        sum_n = 0
        for item in matrix_row:
            sum_n += item
        matrix_row.append(sum_n)
        matrix.append(matrix_row)

[print(''.join(str(a))) for a in matrix]
