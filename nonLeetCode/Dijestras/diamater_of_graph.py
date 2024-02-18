# diamater of graph
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
    # this graph is set up as such 

   # a = {1:[(6,1),(7,1),(2,1)],2:[(3,1)],3:[(5,1),(4,1)],4:[],5:[],6:[],7:[]}
    a = {1:[(2,1),(3,1)],2:[],3:[]}

    # now lets create the graph
    g = Graph()
    for key, val in a.items():
        g.add_node(key)

    for key, val in a.items():   
        for pair in val:
            g.add_edge(key,pair[0],pair[1])
   

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
        
    while len(discoverdSet) < graph.size:
        # pick vertex with minimum value 
        mini = float('inf')
        closest_node = None
        for key, value in distSet.items():
            if value[0] < mini and key not in discoverdSet:
                mini = value[0]
                closest_node = key
            
        if closest_node == 0 or closest_node:
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
    list_of_max_lengths = []
    for item in distSet.values():
        list_of_max_lengths.append(item[1])

        
    length = max(len(arr) for arr in list_of_max_lengths)
    maxs = [r for r in list_of_max_lengths if len(r) == length]
    return maxs

def special_nodes(graph):
    g = graph
    nodes = list(g.get_iterable_dictionary())
    dicts = []
    for i in range(len(nodes)-1):
        d = dij_between(g,nodes[i],nodes[len(nodes)-1])
        dicts.extend(d) # new method for me
    length = max(len(arr) for arr in dicts)
    maxs = [r for r in dicts if len(r) == length]
    specials = [0]* len(nodes)
    for l in maxs:
        # get the spcieals 
        spec = l[0]
        spec2 = l[length-1]
        i = nodes.index(spec)
        j = nodes.index(spec2)
        specials[i] = 1
        specials[j] = 1
    return specials



if __name__ == "__main__":
    # Create a graph object
    g = createGraph()
    
    #print(dij_between(g,2,4))
    # print(dij_between(g,2,6))
    # print(dij_between(g,3,6))
    # print(dij_between(g,4,6))
    # print(dij_between(g,5,6))
    print(special_nodes(g))