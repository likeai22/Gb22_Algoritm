'''
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти
'''
from collections import deque


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length  # Данные о посещении вершины
    weight = [float('inf')] * length  # Вес конкретной вершины, изначально inf
    parent = [-1] * length  # Родитель, пока не знаем -1

    weight[start] = 0  # Путь до вершины, где находимся
    min_weight = 0  # Начальный минимальный вес

    while min_weight < float('inf'):
        is_visited[start] = True
        '''
        1.Обход смежных вершин и запись минимальных весов
        '''
        for i, v in enumerate(graph[start]):
            # print(i, v)
            if v != 0 and not is_visited[i]:
                # если значение вершины !=0 и есть ребро и не посещали - проверить вес
                # если вес до вершины окажется больше чем сумма весов
                # от вершины старт до вершины i + значение которое уже хранится в start,
                # необходимо произвести замену
                if weight[i] > v + weight[start]:  # Если вес для вершины больше, чем сумма от старта до i
                    weight[i] = v + weight[start]  # Записываем более короткий вес
                    parent[i] = start  # Записываем, какая вершина является родительской

        '''
        2.
        '''
        min_weight = float('inf')  # Изменяем значение минимального пути на бесконечность
        for i in range(length):  # Цикл по всем вершина графа
            if min_weight > weight[i] and not is_visited[i]:  # min больше веса пути и вершину не посещали
                min_weight = weight[i]  # сохранили минимальное вес
                start = i  # назначили вершину стартовой

        '''
        3.
        '''

    parent[s] = s

    path = {}
    for i in range(length):
        path[i] = deque([i])

    for i in path:
        if parent[i] != -1:
            if i == s:
                continue
            spam = i

            while spam != s:
                path[i].appendleft(parent[spam])
                spam = parent[spam]
        else:
            path[i] = ['вес 0']

    return weight, path


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]
s = int(input('От какой вершины идём (от 0 до 7 или измените матрицу смежности): '))
# print(dijkstra(g, s))

if 0 <= s <= 7:

    cost, path = dijkstra(g, s)

    print(f'\n Нашли минимальные веса(пути) от вершины {s}:\n {cost}\n')

    print('Проход по вершинам')
    for item in path:
        print(item, ':', *path[item])

else:
    print('Неправильное значение, начните сначала')
