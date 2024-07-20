# Definition for a binary tree node.
from itertools import combinations
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        pathsToLeafs = []

        queue = [(root, [])]


        while queue:
            node, path = queue.pop(0)
            
            new_path = path + [node.val]
            
            if node.left:
                queue.append((node.left, new_path))
                
            if node.right:
                queue.append((node.right, new_path))
                
            if not node.left and not node.right:
                pathsToLeafs.append(new_path)

        pairs = list(combinations(pathsToLeafs, 2))
        
        count = 0
        for i, j in pairs:
            min_length = min(len(i), len(j))
            x = 0
            while x < min_length and i[x] == j[x]:
                x += 1

            i = i[x:]
            j = j[x:]
            
            if len(i) + len(j) < distance:
                count += 1
        return count

           

    
if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    distance = 3
    print(s.countPairs(root, distance))
