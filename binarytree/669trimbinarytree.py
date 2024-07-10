# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        # If current node is out of range, recursively trim either left or right subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # If current node is within range, recursively trim both left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root



def main():
    # p = TreeNode(3,TreeNode(0, None, TreeNode(2, TreeNode(1))),TreeNode(4))
    p = TreeNode(1, None, TreeNode(2))

    a = Solution().trimBST(p, 2, 4)
    print(a)
    

if __name__ == "__main__":
    main()


            
        