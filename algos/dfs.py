# this will have bfs for a tree and a graph 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def findnodeintree(self,root, target):
        # this is spedically to be used with a tree node structure
        # we can do an inorder traverals using this 

        def dfs(root):
            if root.left:
                if dfs(root.left):
                    return True
            if root:
                if root.val == target:
                    return True
            if root.right:
                if dfs(root.right):
                    return True
            return False
        
        return dfs(root)

    def findnodeingraph(self, edges, target):

        visited = set()
        def dfs(start):
            # what we want to do is first explore the child 
            for child in edges[start]:
                if child not in visited:
                    return dfs(child)
            visited.add(start)
            if start == target:
                return True
        
        if dfs(0):
            return True
        return False


if __name__ == '__main__':
    S = Solution()
    graph = [[1,2,3],[3],[5],[4,5],[6],[],[]]
    target = 6
    print(S.findnodeingraph(graph,target))

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






