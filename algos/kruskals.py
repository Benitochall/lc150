class Graph():
    def __init__(self,n) -> None:
        self.vertices = n
        self.graph = []
        self.parents = list(range(n))
        self.size = [1] * n
        pass

    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w])

    def find(self, n):
        # this will return the parent node 
        if n != self.parents[n]:
            self.parents[n] = self.find(self.parents[n])

        return self.parents[n]

    def union(self, node1,node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.size[root1] < self.size[root2]:
                self.parents[root1] = root2
                self.size[root2] += self.size[root1]
            else:
                self.parents[root2] = root1
                self.size[root1] += self.size[root2]

    def KruskalMST(self):
        # this will find the minimum spanning tree

        # step1 sort edges 
        edges = sorted(self.graph, key=lambda x: x[2]) # TODO: remember graph is sorted by key
        e = 0
        i = 0
        total_cost = 0
        edges_used = []

        while e < self.vertices -1:
            # we add each smallest edge to the graph
            # get the first node 
            node1, node2, length = edges[i]

            parent1 = self.find(node1)
            parent2 = self.find(node2)

            if parent1 != parent2:
                self.union(node1, node2)
                total_cost += length
                edges_used.append(edges[i])
                e+=1
            i+=1
        
        return edges_used, total_cost



if __name__ == '__main__':
    g = Graph(4) 
    g.addEdge(0, 1, 10) 
    g.addEdge(0, 2, 6) 
    g.addEdge(0, 3, 5) 
    g.addEdge(1, 3, 15) 
    g.addEdge(2, 3, 4) 
  
    # Function call 
    print(g.KruskalMST())
    pass