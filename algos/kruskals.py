import heapq
class Graph():
    def find(self, n, parents):
        if n != parents[n]:
            n = self.find(parents[n], parents)

        return n

    def union(self, node1, node2, parents, sizes):

        parent1 = self.find(node1,parents)
        parent2 = self.find(node2,parents)

        if parent1 != parent2:
            # two cases 
            if sizes[parent1] >= sizes[parent2]:
                parents[parent2] = parent1
                sizes[parent1] += sizes[parent2]
            else:
                parents[parent1] = parent2
                sizes[parent2] += sizes[parent1]



        return parents, sizes
       

    def KruskalMST(self, graph):
        # create for mst 
        parents = [i for i in range(len(graph))]
        sizes = [1 for _ in range(len(graph))]
        # need to create a list of edges sorted 

        smallestEdges = []

        for i, edges in enumerate(graph):
            for edge in edges:
                end, length = edge
                heapq.heappush(smallestEdges, (length, i, end))

        # now we got all of our edges sorted 
        t_length = 0
        edges_used = []

        while smallestEdges:
            length, startNode, endNode = heapq.heappop(smallestEdges)

            # check to see if the two nodes have the same parent 
            start_node_parent = self.find(startNode, parents)
            end_node_parent = self.find(endNode, parents)

            if start_node_parent == end_node_parent:
                # not use this edge
                continue
            else:
                parents, sizes = self.union(startNode, endNode, parents, sizes)
                t_length+= length
                edges_used.append((startNode,endNode))

        

        return t_length, edges_used



if __name__ == '__main__':
    graph = Graph()
    g = [[(1,10),(2,6), (3,5)], [(3,15)], [(3,4)], []]
  
    # Function call 
    print(graph.KruskalMST(g))

    # should return 19 as the lenght with edges 
    # (0,1)
    # ((0,3)
    # (2,3)
    pass