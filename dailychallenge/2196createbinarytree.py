class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Soultion(object):

    def union(self, graph, parent, child, isLeft):

        # first assign the child to be the child of the parent 

        parent_parent, parent_node = graph[parent]

        _, child_node = graph[child]

        if isLeft:
            parent_node.left = child_node
        else:
            parent_node.right = child_node

        child_parent = parent

        graph[parent] = parent_parent, parent_node
        graph[child] = child_parent, child_node

        return graph

    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        graph = {}
        # (parent, TreeNode)

        for parent, child, isLeft in descriptions:

            # create the parent if it is not in the graph
            if parent not in graph:
                graph[parent] = (None, TreeNode(parent))

            # create the child if it is not in the graph
            if child not in graph:
                graph[child] = (None, TreeNode(child))


            # union the parent and child together

            graph = self.union(graph, parent, child, isLeft)

        root = None
        for key, value in graph.items():
            if value[0] is None:
                root = value[1]
                break
        return root

            






if __name__ == '__main__':
    s = Soultion()
    s.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])