# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        same = False
        if p == None and q == None:
            return True
        while (p and q):
            if p.val != q.val:
                return same
            
            else:
                right = self.isSameTree(p.right, q.right)
                left = self.isSameTree(p.left, q.left)

                return True if right and left else False


def main():
    p = TreeNode(1,TreeNode(2, TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
    q = TreeNode(1,TreeNode(2, TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(8)))

    a = Solution().isSameTree(p,q)
    print(a)
    math.average()
    

if __name__ == "__main__":
    main()
