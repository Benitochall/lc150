# this will have bfs for a tree and a graph 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def findnodeintree(self,root, target):
        # this is spedically to be used with a tree node structure
        queue = [root]

        while queue:
            visit  = queue.pop(0)
            if visit.val == target:
                return True
            else:
                if visit.left:
                    queue.append(visit.left)
                if visit.right:
                    queue.append(visit.right)
        return False

    def findnodeingraph(self, edges, target):
        # the first thing we need to do is create a graph out of edges 
        # idea create a dictionary <node, list of edges>

        visited = []
        queue = [0] # this is the start node

        while queue:
            exploring = queue.pop(0)

            visited.append(exploring)
            if exploring == target:
                return True
            else:
                for neibor in edges[exploring]:
                    if neibor not in visited and neibor not in queue:
                        queue.append(neibor)
        
        return False


if __name__ == '__main__':
    S = Solution()
    # graph = [[1,2,3],[3],[5],[4,5],[6],[],[]]
    # target = 7
    # print(S.findnodeingraph(graph,target))

    # building the tree 
    node8 = TreeNode(8)
    node4 = TreeNode(4, left=node8)
    node5 = TreeNode(5)
    node2 = TreeNode(2, left=node4, right=node5)

    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node3 = TreeNode(3, left=node6, right=node7)

    node1 = TreeNode(1, left=node2, right=node3)
    
    print(S.findnodeintree(node1,10))






