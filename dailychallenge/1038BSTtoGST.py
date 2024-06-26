# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # need to do an inorder traversal of the tree
        visited = []
        visited_dict = {}
        def inOrderTraversal(node):
            if node.right:
                inOrderTraversal(node.right)
            if node:
                if visited:
                    visited_dict[node.val] = TreeNode(node.val + visited[len(visited)-1])
                    visited.append(node.val + visited[len(visited)-1])
                else:
                    visited_dict[node.val] = TreeNode(node.val)
                    visited.append(node.val)
            if node.left:
                inOrderTraversal(node.left)
        inOrderTraversal(root)

        # need to reconstruct the tree
        # how to build a binary search tree from an old one, bst 
        def clone_tree(original_root):
            if not original_root:
                return None
            new_root = TreeNode(original_root.val)
            
            new_root.left = clone_tree(original_root.left)
            new_root.right = clone_tree(original_root.right)
    
            return new_root
        
        return clone_tree(root)
    
if __name__ == '__main__':
    # Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    eight = TreeNode(8)
    seven = TreeNode(7,None,eight)
    five = TreeNode(5)
    six = TreeNode(6,five,seven)

    three = TreeNode(3)
    two = TreeNode(2, None, three)
    zero = TreeNode(0)
    one = TreeNode(1,zero,two)

    root = TreeNode(4, one, six)

    S = Solution()

    S.bstToGst(root)
