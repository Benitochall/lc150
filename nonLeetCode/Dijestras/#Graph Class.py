#Graph Class
class Graph:
    def __init__(self):
        self.graph = {}
        #instantiate the graph 

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
        

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def display(self):
        for node in self.graph:
            print(node, '->', ' -> '.join(map(str, self.graph[node])))

def createGraph():
    # this is how we are passing in the graph 
    n =7
    a = {0:[1,2],1:[3],2:[3],3:[4,5],4:[5,6],5:[6],6:[]}

    # now lets create the graph
    g = Graph()
    for i in range(0,n):
        vals = a[i]
        g.add_node(i)
    for i in range(0,n):
        vals = a[i]
        if vals:
            for edge in list(vals):
                    g.add_edge(i,edge)

    g.display()



if __name__ == "__main__":
    # Create a graph object
    createGraph()
   