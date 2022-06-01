'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа
'''
import networkx as nx
import matplotlib.pyplot as plt


def friends(num):
    if num < 2:
        return ''

    graph = []
    G = nx.DiGraph(graph)

    for i in range(num):
        for j in range(num):
            if i != j:
                graph.append((i, j))
                G.add_edge(i, j)
            # print(i, j)

    # print(graph)
    nx.draw(G, with_labels=True)
    plt.savefig("les_8_task_1.png")
    plt.show()

    return len(graph) // 2


print(friends(int(input('Число друзей, которые встретились: '))))

