# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        from collections import deque

        queue = deque([root])
        averageLevels = []

        while queue:
            level_sum = 0
            level_count = len(queue)
            
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            averageLevels.append(level_sum / level_count)

        return averageLevels


def main():
    p = TreeNode(5,TreeNode(6, TreeNode(8), TreeNode(9)), TreeNode(7, TreeNode(10)))

    a = Solution().averageOfLevels(p)
    print(a)
    math.average()
    

if __name__ == "__main__":
    main()
