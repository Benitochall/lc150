# Definition for a binary tree node.
import math
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # mark this is an important one 
    def kthSmallest(self, root,k):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def inorder_traverse(node):
            # Base case: if the node is None, return an empty list
            if not node:
                return []

            # Recursively traverse the left subtree
            left = inorder_traverse(node.left)
            if len(left) >= k:  # If the kth element is already found in the left subtree
                return left

            # Process the current node
            current = left + [node.val]
            if len(current) == k:  # If the current node is the kth element
                return current

            # Recursively traverse the right subtree
            right = inorder_traverse(node.right)
            return current + right

        # Start the in-order traversal from the root
        result = inorder_traverse(root)
        # The k-th smallest element is the k-1 index in the 0-indexed list
        return result[k - 1] if k <= len(result) else None


def main():
    #p = TreeNode(3,TreeNode(1, None,TreeNode(2)), TreeNode(4))
    #p = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None),TreeNode(4)), TreeNode(6))
    p = TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(7, TreeNode(6), TreeNode(10))))

    a = Solution().kthSmallest(p, 5)
    print(a)
    

if __name__ == "__main__":
    main()
