'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D1%88%D0%B8%D1%80%D0%B8%D0%BD%D1%83
'''


def graph_create(nv, ne):
    lst_neighbors = [[] for _ in range(nv + 1)]

    for _ in range(ne):
        u, v = map(int, input().split())
        lst_neighbors[u] += [v]

    return lst_neighbors


def dfs(graph, start):
    # e = [[], [2, 3, 4], [1, 4, 5], [1, 4], [1, 2, 3, 5], [2, 4]]
    # start = int(input())
    queue = []
    not_visited = 0
    added = 1
    is_visited = 2
    status = [not_visited for _ in range(num_v + 1)]

    queue += [start]
    status[start] = added
    idx = 0
    while idx < len(queue):
        vertex = queue[idx]
        status[vertex] = is_visited
        idx += 1
        for neighbor in graph[vertex]:
            if status[neighbor] is not_visited:
                queue += [neighbor]
                status[neighbor] = added
    return queue


num_v = int(input())  # количество вершин
num_e = int(input())  # количество рёбер
g = graph_create(num_v, num_e)
print(g)
'''
Списки смежности:
W[1] = [2, 3, 4] 
W[2] = [1, 4, 5] 
W[3] = [1, 4] 
W[4] = [1, 2, 3, 5] 
W[5] = [2, 4]

Порядок ввода:
5
14
1 2
1 3
1 4
2 1
2 4
2 5
3 1
3 4
4 1
4 2
4 3
4 5
5 2
5 4

Результат:
[[], [2, 3, 4], [1, 4, 5], [1, 4], [1, 2, 3, 5], [2, 4]]
'''
# g = [[], [2, 3, 4], [1, 4, 5], [1, 4], [1, 2, 3, 5], [2, 4]]
st = int(input())
d = dfs(g, st)
print(d)
