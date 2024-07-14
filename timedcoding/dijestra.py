# this is the test enviorment for dijestras shortest path algo
# the graph will always stay the same
import heapq

class Graph:
    def __init__(self, g) -> None:
        self.graph = g

    def dijestras(self, node):
        pass


if __name__ == '__main__':
    graph = [
    [(1, 7), (2, 9), (3, 14)],   # Node 0 is connected to nodes 1, 2, and 3 with distances 7, 9, and 14 respectively
    [(0, 7), (2, 10), (4, 15)],  # Node 1 is connected to nodes 0, 2, and 4 with distances 7, 10, and 15 respectively
    [(0, 9), (1, 10), (3, 2), (4, 11)],  # Node 2 is connected to nodes 0, 1, 3, and 4 with distances 9, 10, 2, and 11 respectively
    [(0, 14), (2, 2), (5, 9)],  # Node 3 is connected to nodes 0, 2, and 5 with distances 14, 2, and 9 respectively
    [(1, 15), (2, 11), (5, 6)],  # Node 4 is connected to nodes 1, 2, and 5 with distances 15, 11, and 6 respectively
    [(3, 9), (4, 6)]           # Node 5 is connected to nodes 3 and 4 with distances 9 and 6 respectively
]

    # answer from 0 should be   
    #[0, 7, 9, 11, 20, 20]

    G = Graph(graph)

    print(G.dijestras(0))

