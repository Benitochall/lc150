# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # the idea in level oder traversal is to create a queue of nodes that need to be traversed

        visited = []
        queue = [root]
        buffer = []


        while len(queue) > 0:
            level_size = len(queue)
            buffer = []

            for _ in range(level_size):
                # need to pop
                val = queue.pop(0)
                if val:
                    buffer.append(val.val)
                    if val.left:
                        queue.append(val.left)
                    if val.right:
                        queue.append(val.right)
            visited.append(buffer)
        return visited
            

if __name__ == '__main__':

    root = TreeNode(3, TreeNode(9),TreeNode(20,TreeNode(15), TreeNode(17)))
    s = Solution()
    s.levelOrder(root)

    
