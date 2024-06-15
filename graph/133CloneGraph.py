class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        # The implementation of cloneGraph will go here.
        discoverd_nodes = {}
        def dfs(node):
            # for each node 
            discoverd_nodes.update({node.val:node.neighbors})
            for neighbor in node.neighbors:
                if neighbor.val not in discoverd_nodes:
                    dfs(neighbor)
        dfs(node)
        ajacency_list = [0] * len(discoverd_nodes)
        for key, val in discoverd_nodes.items():
            ajacency_list[key-1] = [node.val for node in val]

        # now need to build a graph 
        nodes = [Node(i+1) for i in enumerate(len(ajacency_list))]

        for i, neighbors in enumerate(ajacency_list):
            nodes[i].neighbors = [nodes[j-1] for j in neighbors] 
        
        return nodes[0]




        pass


# Helper function to create a graph from an adjacency list
def createGraph(adjList):
    if not adjList:
        return None

    nodes = [Node(i + 1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]
   

if __name__ == '__main__':
    # Adjacency list representation of the graph
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

    # Create the graph
    original_graph = createGraph(adjList)

    # Create a Solution object
    s = Solution()

    # Clone the graph
    cloned_graph = s.cloneGraph(original_graph)

    # Print the original graph
    print("Original graph:")
    printGraph(original_graph)

    # Print the cloned graph
    print("Cloned graph:")
    printGraph(cloned_graph)
