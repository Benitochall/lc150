#Dijestras with needing to know path
#Dijestras 
import copy
class Graph:
    def __init__(self):
        self.graph = {}
        self.size = 0
        #instantiate the graph 

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            self.size+=1

        

    def add_edge(self, node1, node2,distance):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append((node2, distance))
            self.graph[node2].append((node1, distance))

    def display(self):
        for node in self.graph:
            print(node, '->', ' -> '.join(map(str, self.graph[node])))
    def get_node(self,node):
        return self.graph[node]
    def get_iterable_dictionary(self):
        return dict(self.graph)


def createGraph():
    # this is how we are passing in the graph 
    n =7
    # this graph is set up as such 

    a = {0:[(1,2),(2,6)],1:[(3,5)],2:[(3,8)],3:[(4,10),(5,15)],4:[(5,6),(6,2)],5:[(6,6)],6:[]}

    # now lets create the graph
    g = Graph()
    for i in range(0,n):
        vals = a[i]
        g.add_node(i)
    for i in range(0,n):
        vals = a[i]
        if vals:
            for edge in list(vals):
                    #print(edge)
                    g.add_edge(i,edge[0],edge[1])

    #g.display()
    return g
def dij_between(graph, node1,node2):
    # implment dijestreas
    distSet = {}
    # turn the dist set into a a dictionary 
    a = graph.get_iterable_dictionary()
    nodes = list(a.keys())

    for i in range(graph.size):
        # adding dict 
        if nodes[i] == node1:
            new_dict = {nodes[i]:(0,[nodes[i]])}
        else:
            new_dict = {nodes[i]:(float('inf'),[])}
        distSet.update(new_dict)
        
    discoverdSet =[node1]
    #E print(sptSet)
    # now we have our set
    #go through current edges add to ajacency matrix
    # keeping track of length and path
    # add the first ajacent edges
    ajacents_first = a[node1]
     #update ajacent value distances 
    # need to get the array out of dict
    key,value = distSet[node1]
    for item in ajacents_first:
        # need to update the distances of the first node 
        path = [value[0],item[0]]
        new_dict = {item[0]:(item[1],path)}
        distSet.update(new_dict)
        
    while len(discoverdSet) < graph.size and node2 not in discoverdSet:
        # pick vertex with minimum value 
        mini = float('inf')
        closest_node = None
        for key, value in distSet.items():
            if value[0] < mini and key not in discoverdSet:
                mini = value[0]
                closest_node = key
            
        if closest_node:
            discoverdSet.append(closest_node)
            # now we have appended the closest node 
            # need to get its distance 
            ajacents = graph.get_node(closest_node)

            # this is the distance to the parent
            current_dist = distSet[closest_node][0]

            # need to get the current path
            path = copy.deepcopy(distSet[closest_node][1])
            # need to find the index of the current node in the path
            i = path.index(closest_node)
            path = path[:i+1]
           
            for item in ajacents:
                if item[0] in discoverdSet:
                    continue
                if distSet[item[0]][0] > item[1] + current_dist:
                    length = item[1] + current_dist
                    # update the path
                    add_path = copy.deepcopy(path)
                    add_path.append(item[0])
                    new_dict = {item[0]:(length,add_path)}
                    distSet.update(new_dict)
    return distSet



if __name__ == "__main__":
    # Create a graph object
    g = createGraph()
    
    print(dij_between(g,0,6))
