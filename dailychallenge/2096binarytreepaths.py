# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """

        # need to go find the path to the start and to the dest

        def dfs_path(root, val, curr_path):
            if not root:
                return False
            
            if root.val == val:
                return (True, curr_path)
            
            if root.left:
                if dfs_path(root.left, val, curr_path):
                    curr_path.insert(0,'L')
                    return  (True, curr_path)
                
            if root.right:
                if dfs_path(root.right, val, curr_path):
                    curr_path.insert(0, 'R')
                    return (True, curr_path)
                
        _ , start_path = dfs_path(root, startValue, [])
        _, end_path = dfs_path(root, destValue, [])

        i = 0

        if start_path and end_path:

            while start_path[i] == end_path[i]:
                start_path.pop(0)
                end_path.pop(0)

        start_path = ['U' for _ in range(len(start_path))]
        a = ''.join(start_path)
        b = ''.join(end_path)

        return a +b
            

if __name__ == '__main__':
    s = Solution()
    #root = TreeNode(5, TreeNode(1, TreeNode(3), None), TreeNode(2, TreeNode(6), TreeNode(4)))
    root = TreeNode(2,TreeNode(1))



    print(s.getDirections(root,2,1))
        