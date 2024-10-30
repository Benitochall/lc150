import heapq
class Graph():
    def __init__(self,g) -> None:
        self.graph = g
        self.size = len(g)

    def dijestras(self, node):

        visited = []
        info_set = [(float('inf'),[]) for _ in range(self.size)]
        dist_pq = [(0,node)]
        info_set[node] = (0, [])
        heapq.heapify(dist_pq)

        while dist_pq:
            dist, exploring_node = heapq.heappop(dist_pq)
            path = info_set[exploring_node][1]

            if dist > info_set[exploring_node][0]:
                # we have already found the optimal path
                continue
            # now go get all of the nodes neibors

            for node, dnode in self.graph[exploring_node]:
                # calculate distance from the source 
                if node in visited:
                    continue
                curr_dist = info_set[node][0]
                calc_dist = dist + dnode

                if calc_dist < curr_dist:
                    # we want to calculate path
                    new_p = path + [exploring_node]
                    info_set[node] = (calc_dist, new_p)
                    heapq.heappush(dist_pq, (calc_dist, node))

            visited.append(exploring_node)

        return info_set


if __name__ == '__main__':

    graph = [
    [(1, 7), (2, 9), (4, 14)],          # Node 0
    [(0, 7), (2, 10), (3, 15)],         # Node 1
    [(0, 9), (1, 10), (3, 11), (4, 2)], # Node 2
    [(1, 15), (2, 11), (4, 6)],         # Node 3
    [(0, 14), (2, 2), (3, 6)]           # Node 4
]
    g = Graph(graph)

    print(g.dijestras(0))